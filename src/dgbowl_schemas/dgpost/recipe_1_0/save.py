from pydantic import BaseModel, Field
from typing import Literal


class Save(BaseModel, extra="forbid", populate_by_name=True):
    table: str
    as_: str = Field(alias="as")
    type: Literal["pkl", "json", "xlsx", "csv"] = None
    sigma: bool = True
