from pydantic import BaseModel, Field
from typing import Literal


class Load(BaseModel, extra="forbid", populate_by_name=True):
    as_: str = Field(alias="as")
    path: str
    type: Literal["datagram", "table"] = "datagram"
    check: bool = True
