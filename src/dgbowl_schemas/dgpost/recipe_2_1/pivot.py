from pydantic import BaseModel, Field, Extra
from typing import Sequence, Any, Dict, Literal


class Pivot(BaseModel, extra=Extra.forbid, allow_population_by_field_name=True):
    table: str
    on: str
    columns: Sequence[str] = None
    timestamp: Literal["first", "last", "mean"] = "first"
