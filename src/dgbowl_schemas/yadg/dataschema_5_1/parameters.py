from typing import Union

from pydantic import BaseModel

from .timestamp import UTS, TimeDate, Timestamp


class Parameters(BaseModel, extra="forbid"):
    """Empty parameters specification with no extras allowed."""


Timestamps = Union[Timestamp, TimeDate, UTS]
