from pydantic import BaseModel

from .timestamp import UTS, TimeDate, Timestamp


class Parameters(BaseModel, extra="forbid"):
    """Empty parameters specification with no extras allowed."""


Timestamps = Timestamp | TimeDate | UTS
