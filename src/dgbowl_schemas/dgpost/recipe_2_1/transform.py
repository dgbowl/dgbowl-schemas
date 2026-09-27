from collections.abc import Sequence
from typing import Any

from pydantic import BaseModel, Field


class Transform(BaseModel, extra="forbid", populate_by_name=True):
    """Calculate and otherwise transform the data in the tables."""

    table: str
    """The name of the table loaded in memory to be transformed."""

    with_: str = Field(alias="with")
    """The name of the transform function from **dgpost's** transform library."""

    using: Sequence[dict[str, Any]]
    """Specification of any parameters required by the transform function."""
