from pydantic import BaseModel
from typing import Optional


class TimestampSpec(BaseModel, extra="forbid"):
    index: Optional[int] = None
    format: Optional[str] = None


class Timestamp(BaseModel, extra="forbid"):
    timestamp: TimestampSpec


class UTS(BaseModel, extra="forbid"):
    uts: TimestampSpec


class TimeDate(BaseModel, extra="forbid"):
    date: Optional[TimestampSpec] = None
    time: Optional[TimestampSpec] = None
