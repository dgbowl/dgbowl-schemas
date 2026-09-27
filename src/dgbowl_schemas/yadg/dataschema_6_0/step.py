from typing import Optional, Union

from pydantic import BaseModel

from .externaldate import ExternalDate
from .filetype import FileTypes
from .input import Input


class Step(BaseModel, extra="forbid"):
    extractor: Union[FileTypes]
    input: Input
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None
