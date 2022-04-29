from pydantic import BaseModel, Field, validator, root_validator, Extra
from typing import Optional, Union, Sequence, Mapping, Literal
import logging

logger = logging.getLogger(__name__)

from .parameters import (
    Dummy,
    BasicCSV,
    MeasCSV,
    XPSTrace,
    ChromTrace,
    ElectroChem,
    FlowData,
    MassTrace,
    QFTrace,
)
from .externaldate import ExternalDate
from .input import Input


class Metadata(BaseModel, extra=Extra.forbid):
    provenance: str
    version: str
    timezone: str = "localtime"
    provenance_metadata: Optional[Mapping]

    @root_validator(pre=True, allow_reuse=True)
    def check_version(cls, values):
        version = values.get("version")
        if version is None:
            for k in {"dataschema_version", "schema_version"}:
                if k in values:
                    version = values.pop(k)
        values["version"] = version
        return values


class Step(BaseModel, extra=Extra.forbid):
    parser: Literal[
        "dummy",
        "basiccsv",
        "meascsv",
        "xpstrace",
        "chromtrace",
        "electrochem",
        "flowdata",
        "masstrace",
        "qftrace",
    ]
    input: Input
    tag: str = None
    parameters: Union[
        Dummy,
        BasicCSV,
        MeasCSV,
        XPSTrace,
        ChromTrace,
        ElectroChem,
        FlowData,
        MassTrace,
        QFTrace,
    ] = Field(default=None, discriminator="parser")
    externaldate: Optional[ExternalDate]
    export: Optional[str]

    @root_validator(pre=True, allow_reuse=True)
    def check_import(cls, values):
        input = values.get("input")
        if input is None and "import" in values:
            logger.warning(
                "Specifying 'input' files of a Step using the 'import' key is "
                "deprecated and may stop working in future versions of 'dataschema'."
            )
            input = values.pop("import")
        if input is None:
            raise ValueError("The 'input' section has to be specified for each Step.")
        values["input"] = input
        return values

    @root_validator(pre=True, allow_reuse=True)
    def copy_parser_to_params(cls, values):
        params = values.get("parameters")
        if params is not None:
            values["parameters"]["parser"] = values["parser"]
        return values

    # @validator("parser")
    # def copy_parser_to_params(cls, v, values):
    #    values["parameters"]["parser"] = v
    #    return v, values

    # @validator("externaldate", always=True, pre=True)
    # def default_externaldate(cls, v):
    #    return v or {}


class DataSchema(BaseModel, extra=Extra.forbid):
    """
    Schema of the Dataschema object.

    Must contain:

    - a 'metadata' entry containing a Metadata object
    - a 'steps' entry containing a list of Step objects

    """

    metadata: Metadata
    steps: Sequence[Step]
