from pydantic import BaseModel, Extra, Field
from abc import ABC
from typing import Optional, Literal, Union

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


class FileType(BaseModel, ABC, extra=Extra.forbid):
    """Template ABC for parser classes."""

    filetype: str
    timezone: Optional[str]
    locale: Optional[str]
    encoding: Optional[str]


class EClab_MPR(FileType):
    filetype: Literal["eclab.mpr", "marda:biologic-mpr"]


class EClab_MPT(FileType):
    filetype: Literal["eclab.mpt", "marda:biologic-mpt"]
    encoding: str = "windows-1252"


FileTypes = Annotated[
    Union[
        EClab_MPR,
        EClab_MPT,
    ],
    Field(discriminator="filetype"),
]
