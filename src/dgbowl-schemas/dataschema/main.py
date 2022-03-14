from pydantic import BaseModel, ValidationError, validator, root_validator
from pydantic.dataclasses import dataclass
import os
from typing import Optional, List
import logging

logger = logging.getLogger(__name__)


class Metadata(BaseModel):
    provenance: str
    version: str
    
    @root_validator(pre=True)
    def check_version(cls, values):
        version = values.get("version")
        if version is None:
            version = values.get("dataschema_version")
        if version is None:
            version = values.get("schema_version")
        values["version"] = version
        return values


class Input(BaseModel):
    files: List[str] = None
    folders: List[str] = None
    prefix: str = None
    suffix: str = None
    contains: str = None
    exclude: str = None
    encoding: str = "UTF-8"

    @root_validator(pre=True)
    def check_paths(cls, values):
        files, folders = values.get("files"), values.get("folders")
        if files is not None and folders is not None:
            raise ValueError("cannot specify both 'files' and 'folders'")
        elif files is None and folders is None:
            raise ValueError("must specify either 'files' or 'folders'")
        return values
    
    def paths(self) -> List[str]:
        if self.files is not None:
            paths = self.files
        else:
            paths = [file for sublist in self.folders for file in os.listdir(sublist)]
        ret = []
        for path in paths:
            inc = True
            if self.prefix is not None and not path.startswith(self.prefix):
                inc = False
            if self.suffix is not None and not path.endswith(self.suffix):
                inc = False
            if self.contains is not None and self.contains not in path:
                inc = False
            if self.exclude is not None and self.exclude in path:
                inc = False
            if inc:
                ret.append(path)
        return ret
        

class ExternalDate(BaseModel):
    using: dict
    mode: str = "add"

    @root_validator(pre=True)
    def check_using(cls, values):
        using = values.get("using")
        if using is None:
            logger.warning(
                "Specifying 'using' parameter of ExternalDate via the 'from' key is "
                "deprecated and may stop working in future versions of 'dataschema'."
            )
            using = values.get("from")
        if using is None:
            using = {"filename": {"format": "%Y-%m-%d-%H-%M-%S", "len": 19}}
        values["using"] = using
        return values

    @validator('mode')
    def mode_is_known(cls, v):
        if v not in {"add", "replace"}:
            raise ValueError(
                "The provided ExeternalDate 'mode' type '{v}' was not understood."
            )


class Step(BaseModel):
    parser: str
    input: Input
    tag: str = None
    parameters: dict = None
    externaldate: ExternalDate

    @root_validator(pre=True)
    def check_import(cls, values):
        input = values.get("input")
        if input is None and "import" in values:
            logger.warning(
                "Specifying 'input' files of a Step using the 'import' key is "
                "deprecated and may stop working in future versions of 'dataschema'."
            )
            input = values.get("import")
        if input is None:
            raise ValueError(
                "The 'input' section has to be specified for each Step."
            )
        values["input"] = input
        return values
    
    @root_validator(pre=True)
    def check_externaldate(cls, values):
        ed = values.get("externaldate")
        if ed is None:
            ed = {}
        values["externaldate"] = ed
        return values
    
    @validator('parser')
    def parser_is_known(cls, v):
        if v not in {
            "chromtrace", 
            "masstrace",
            "qftrace",
            "basiccsv",
            "meascsv",
            "flowdata",
            "electrochem",
            "dummy",
        }:
            raise ValueError(
                "The name '{v}' provided as a 'parser' in Step was not understood."
            )
        return v


class Dataschema(BaseModel):
    metadata: Metadata
    steps: list[Step]

# Dataschema(**kwargs)