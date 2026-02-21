from pydantic import BaseModel
from typing import Optional, Mapping, Literal, Any


class Metadata(BaseModel, extra="forbid"):
    class Provenance(BaseModel, extra="forbid"):
        type: str
        metadata: Optional[Mapping[str, Any]] = None

    provenance: Provenance
    version: Literal["4.1", "4.1.0", "4.1.1", "4.1.2", "4.1.3"]
    timezone: str = "localtime"
