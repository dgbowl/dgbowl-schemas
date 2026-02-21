from pydantic import BaseModel
from typing import Literal, Optional, Union


class ExternalDateFile(BaseModel, extra="forbid"):
    class Content(BaseModel, extra="forbid"):
        path: str
        type: str
        match: Optional[str] = None

    file: Content


class ExternalDateFilename(BaseModel, extra="forbid"):
    class Content(BaseModel, extra="forbid"):
        format: str
        len: int

    filename: Content


class ExternalDateISOString(BaseModel, extra="forbid"):
    isostring: str


class ExternalDateUTSOffset(BaseModel, extra="forbid"):
    utsoffset: float


class ExternalDate(BaseModel, extra="forbid"):
    using: Union[
        ExternalDateFile,
        ExternalDateFilename,
        ExternalDateISOString,
        ExternalDateUTSOffset,
    ]
    mode: Literal["add", "replace"] = "add"
