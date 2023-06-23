from pydantic import BaseModel, Extra, Field
from typing import Sequence, Literal


class Pivot(BaseModel, extra=Extra.forbid, allow_population_by_field_name=True):
    table: str
    as_: str = Field(alias="as")
    using: str
    columns: Sequence[str] = None
    timestamp: Literal["first", "last", "mean"] = "first"
