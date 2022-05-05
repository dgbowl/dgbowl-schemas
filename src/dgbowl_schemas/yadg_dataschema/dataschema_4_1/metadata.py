from pydantic import BaseModel, Extra
from typing import Optional, Mapping, Literal


class Metadata(BaseModel, extra=Extra.forbid):
    class Provenance(BaseModel, extra=Extra.forbid):
        type: str
        metadata: Optional[Mapping[str, str]]

    provenance: Provenance
    version: Literal["4.1"]
    timezone: str = "localtime"
