from pydantic import BaseModel, Field
from typing import Literal


class Metadata(BaseModel, extra="forbid", populate_by_name=True):
    version: Literal["4.0", "4.0.0", "4.0.1"] = Field(alias="schema_version")
    provenance: str
    timezone: str = "localtime"
