from pydantic import BaseModel, Field, field_validator
from typing import Literal, Optional, Union
import pint


class Settings(BaseModel, extra="forbid"):
    """
    Specification of *job* configuration for tomato.
    """

    class Output(BaseModel, extra="forbid"):
        """
        Provide the ``path`` and ``prefix`` for the final FAIR-data archive of the *job*.
        """

        path: Optional[str] = None
        prefix: Optional[str] = None

    class Snapshot(BaseModel, extra="forbid"):
        """
        Provide the ``frequency``, ``path`` and ``prefix`` to configure the snapshotting
        functionality of tomato.
        """

        path: Optional[str] = None
        prefix: Optional[str] = None
        snapshot_interval: Union[float, str] = 3600.0

        @field_validator("snapshot_interval", mode="after")
        @classmethod
        def convert_str_to_seconds(cls, v: Union[str, float]) -> float:
            if isinstance(v, str):
                return pint.Quantity(v).to("seconds").m
            else:
                return v

    unlock_when_done: bool = False
    """set *pipeline* as ready when *job* finishes successfully"""

    verbosity: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "WARNING"

    output: Output = Field(default_factory=Output)
    """Options for final NetCDF data output."""

    snapshot: Optional[Snapshot] = None
    """Options for periodic snapshotting."""
