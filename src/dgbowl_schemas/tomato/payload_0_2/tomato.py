from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class Tomato(BaseModel, extra="forbid"):
    """
    Specification of *job* configuration for tomato.
    """

    class Output(BaseModel, extra="forbid"):
        """
        Provide the ``path`` and ``prefix`` for the final FAIR-data archive of the *job*.
        """

        path: str | None = None
        prefix: str | None = None

    class Snapshot(BaseModel, extra="forbid"):
        """
        Provide the ``frequency``, ``path`` and ``prefix`` to configure the snapshotting
        functionality of tomato.
        """

        path: str | None = None
        prefix: str | None = None
        frequency: int = 3600

    unlock_when_done: bool = False
    """set *pipeline* as ready when *job* finishes successfully"""

    verbosity: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "WARNING"

    output: Output = Field(default_factory=Output)
    """Options for final FAIR data output."""

    snapshot: Snapshot | None = None
    """Options for periodic snapshotting."""
