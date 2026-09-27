from typing import Literal

from pydantic import BaseModel, Field


class Save(BaseModel, extra="forbid", populate_by_name=True):
    table: str
    as_: str = Field(alias="as")
    type: Literal["pkl", "json", "xlsx", "csv"] | None = None
    sigma: bool = True
