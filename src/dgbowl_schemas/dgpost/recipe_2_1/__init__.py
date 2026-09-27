from collections.abc import Sequence
from typing import Literal

from pydantic import BaseModel

from .extract import Extract
from .load import Load
from .pivot import Pivot
from .plot import Plot
from .save import Save
from .transform import Transform


class Recipe(BaseModel, extra="forbid"):
    """
    A :class:`pydantic.BaseModel` implementing ``Recipe-2.1`` model for :mod:`dgpost`.
    """

    version: Literal["2.1"]

    load: Sequence[Load] | None = None
    """Select external files (``NetCDF`` or ``json`` datagrams, ``pkl`` tables) to load."""

    extract: Sequence[Extract] | None = None
    """Extract columns from loaded files into tables, interpolate as necessary."""

    pivot: Sequence[Pivot] | None = None
    """Reorder tables by grouping rows into arrays using columns as indices."""

    transform: Sequence[Transform] | None = None
    """Calculate and otherwise transform the data in the tables."""

    plot: Sequence[Plot] | None = None
    """Plot data from a single table."""

    save: Sequence[Save] | None = None
    """Save a table into an external (``pkl``, ``xlsx``) file."""
