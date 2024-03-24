from pydantic import BaseModel
from typing import Optional
from .externaldate import ExternalDate
from .input import Input
from .filetype import FileTypes


class Step(BaseModel, extra="forbid"):
    extractor: FileTypes
    input: Input
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None
