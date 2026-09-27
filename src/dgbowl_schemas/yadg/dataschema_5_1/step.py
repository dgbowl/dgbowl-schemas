from __future__ import annotations

from pydantic import BaseModel

from .externaldate import ExternalDate
from .filetype import FileTypes
from .input import Input


class Step(BaseModel, extra="forbid"):
    extractor: FileTypes
    input: Input
    tag: str | None = None
    externaldate: ExternalDate | None = None
