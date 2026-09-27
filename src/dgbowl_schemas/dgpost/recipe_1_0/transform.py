from collections.abc import Sequence
from typing import Any

from pydantic import BaseModel, Field


class Transform(BaseModel, extra="forbid", populate_by_name=True):
    table: str
    with_: str = Field(alias="with")
    using: Sequence[dict[str, Any]]
