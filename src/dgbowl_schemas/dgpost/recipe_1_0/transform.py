from pydantic import BaseModel, Field
from typing import Sequence, Any, Dict


class Transform(BaseModel, extra="forbid", populate_by_name=True):
    table: str
    with_: str = Field(alias="with")
    using: Sequence[Dict[str, Any]]
