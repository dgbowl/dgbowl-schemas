from pydantic import BaseModel


class TimestampSpec(BaseModel, extra="forbid"):
    """Specification of the column index and string format of the timestamp."""

    index: int | None = None
    format: str | None = None


class Timestamp(BaseModel, extra="forbid"):
    """Timestamp from a column containing a single timestamp string."""

    timestamp: TimestampSpec


class UTS(BaseModel, extra="forbid"):
    """Timestamp from a column containing a Unix timestamp."""

    uts: TimestampSpec


class TimeDate(BaseModel, extra="forbid"):
    """Timestamp from a separate date and/or time column."""

    date: TimestampSpec | None = None
    time: TimestampSpec | None = None
