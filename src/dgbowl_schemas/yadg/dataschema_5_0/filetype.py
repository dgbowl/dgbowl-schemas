from pydantic import BaseModel, Extra, Field, validator
from abc import ABC
from typing import Optional, Literal, Union
import tzlocal
import locale


class FileType(BaseModel, ABC, extra=Extra.forbid):
    """Template ABC for parser classes."""

    filetype: str
    timezone: str = "localtime"
    locale: Optional[str]
    encoding: Optional[str]

    @validator("timezone", always=True)
    @classmethod
    def timezone_resolve_localtime(cls, v):
        if v == "localtime":
            v = tzlocal.get_localzone_name()
        return v

    @validator("locale", always=True)
    @classmethod
    def locale_set_default(cls, v):
        if v is None:
            v = ".".join(locale.getlocale())
        return v


class EClab_mpr(FileType):
    filetype: Literal["eclab.mpr", "marda:biologic-mpr"]


class EClab_mpt(FileType):
    filetype: Literal["eclab.mpt", "marda:biologic-mpt"]
    encoding: str = "windows-1252"


class Tomato_json(FileType):
    filetype: Literal["tomato.json"]


class FileTypeFactory(BaseModel):
    filetype: Union[
        EClab_mpr,
        EClab_mpt,
        Tomato_json,
    ] = Field(..., discriminator="filetype")
