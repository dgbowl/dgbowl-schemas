from __future__ import annotations

from pydantic import BaseModel


class TimestampSpec(BaseModel, extra="forbid"):
    index: int | None = None
    format: str | None = None


class Timestamp(BaseModel, extra="forbid"):
    timestamp: TimestampSpec


class UTS(BaseModel, extra="forbid"):
    uts: TimestampSpec


class TimeDate(BaseModel, extra="forbid"):
    date: TimestampSpec | None = None
    time: TimestampSpec | None = None
