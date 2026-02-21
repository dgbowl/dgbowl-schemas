from pydantic import BaseModel
from typing import Optional, Union

from .timestamp import Timestamp, TimeDate, UTS


class Tol(BaseModel, extra="forbid"):
    atol: Optional[float] = None
    rtol: Optional[float] = None


Timestamps = Union[Timestamp, TimeDate, UTS]
