import logging
from typing import Literal

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class ExternalDateFile(BaseModel, extra="forbid"):
    class Content(BaseModel, extra="forbid"):
        path: str
        type: str
        match: str | None = None

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


class ExternalDate(BaseModel, extra="forbid", populate_by_name=True):
    using: (
        ExternalDateFile
        | ExternalDateFilename
        | ExternalDateISOString
        | ExternalDateUTSOffset
    ) = Field(alias="from")
    mode: Literal["add", "replace"] = "add"
