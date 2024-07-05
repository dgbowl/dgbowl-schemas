from pydantic import BaseModel, Field
from typing import Literal, Optional


class Tomato(BaseModel, extra="forbid"):
    """
    Specification of *job* configuration for tomato.
    """

    class Output(BaseModel, extra="forbid"):
        """
        Provide the ``path`` and ``prefix`` for the final FAIR-data archive of the *job*.
        """

        path: str = None
        prefix: str = None

    class Snapshot(BaseModel, extra="forbid"):
        """
        Provide the ``frequency``, ``path`` and ``prefix`` to configure the snapshotting
        functionality of tomato.
        """

        path: str = None
        prefix: str = None
        frequency: int = 3600

    unlock_when_done: bool = False
    """set *pipeline* as ready when *job* finishes successfully"""

    verbosity: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "WARNING"

    output: Output = Field(default_factory=Output)
    """Options for final FAIR data output."""

    snapshot: Optional[Snapshot] = None
    """Options for periodic snapshotting."""
