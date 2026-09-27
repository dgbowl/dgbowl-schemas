from __future__ import annotations

from typing import Union

from pydantic import BaseModel

from .timestamp import UTS, TimeDate, Timestamp


class Tol(BaseModel, extra="forbid"):
    """Specification of absolute and relative tolerance/error."""

    atol: float | None = None
    rtol: float | None = None


Timestamps = Union[Timestamp, TimeDate, UTS]
