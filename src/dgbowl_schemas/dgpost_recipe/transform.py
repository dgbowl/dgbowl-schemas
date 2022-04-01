from pydantic import BaseModel, Field
from typing import Sequence, Any


class Transform(BaseModel, extra="forbid"):
    table: str
    with_: str = Field(alias="with")
    using: Sequence[dict[str, Any]]
