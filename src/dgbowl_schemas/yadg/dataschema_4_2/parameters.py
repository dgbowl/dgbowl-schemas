from typing import Optional, Union

from pydantic import BaseModel

from .timestamp import UTS, TimeDate, Timestamp


class Tol(BaseModel, extra="forbid"):
    """Specification of absolute and relative tolerance/error."""

    atol: Optional[float] = None
    rtol: Optional[float] = None


Timestamps = Union[Timestamp, TimeDate, UTS]
