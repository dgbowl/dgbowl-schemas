from pydantic import BaseModel, Extra
from typing import Optional, Union

from .timestamp import Timestamp, TimeDate, UTS


class Parameters(BaseModel, extra=Extra.forbid):
    """Empty parameters specification with no extras allowed."""

    pass


Timestamps = Union[Timestamp, TimeDate, UTS]
