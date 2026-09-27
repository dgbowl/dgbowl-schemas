from typing import Literal

from pydantic import BaseModel, Field


class Load(BaseModel, extra="forbid", populate_by_name=True):
    as_: str = Field(alias="as")
    path: str
    type: Literal["datagram", "table"] = "datagram"
    check: bool = True
