from pydantic import BaseModel

from .timestamp import UTS, TimeDate, Timestamp


class Tol(BaseModel, extra="forbid"):
    atol: float | None = None
    rtol: float | None = None


Timestamps = Timestamp | TimeDate | UTS
