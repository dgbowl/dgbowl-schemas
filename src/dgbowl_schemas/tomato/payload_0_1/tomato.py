from typing import Literal

from pydantic import BaseModel, Field


class Tomato(BaseModel, extra="forbid"):
    class Output(BaseModel, extra="forbid"):
        path: str = None
        prefix: str = None

    unlock_when_done: bool = False
    verbosity: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "WARNING"
    output: Output = Field(default_factory=Output)
