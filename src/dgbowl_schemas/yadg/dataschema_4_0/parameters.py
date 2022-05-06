from pydantic import BaseModel, Extra, Field
from typing import Literal, Optional, Union, Any, Mapping

from .timestamp import Timestamp, TimeDate, UTS


class Tol(BaseModel, extra=Extra.forbid):
    atol: Optional[float]
    rtol: Optional[float]

Timestamps = Union[Timestamp, TimeDate, UTS]