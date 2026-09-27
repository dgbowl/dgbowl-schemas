from collections.abc import Sequence
from typing import Any, Literal

from pydantic import BaseModel, Field


class SeriesIndex(BaseModel, extra="forbid"):
    from_zero: bool = True
    to_units: str | None = None


class Series(BaseModel, extra="allow"):
    y: str
    x: str | None = None
    kind: Literal["scatter", "line", "errorbar"] = "scatter"
    index: SeriesIndex | None = SeriesIndex()


class AxArgs(BaseModel, extra="allow"):
    cols: tuple[int, int] | None = None
    rows: tuple[int, int] | None = None
    series: Sequence[Series]
    methods: dict[str, Any] | None = None
    legend: bool = False


class PlotSave(BaseModel, extra="allow", populate_by_name=True):
    as_: str = Field(alias="as")
    tight_layout: dict[str, Any] | None = None


class Plot(BaseModel, extra="forbid"):
    """Plot data from a single table."""

    table: str
    """The name of the table loaded in memory to be plotted."""

    nrows: int = 1
    """Number of rows in the figure grid."""

    ncols: int = 1
    """Number of columns in the figure grid."""

    fig_args: dict[str, Any] | None = None
    """Any optional method calls for the figure; passed to ``matplotlib``."""

    ax_args: Sequence[AxArgs]
    """Specifications of the figure axes, including selection of data for the plots."""

    style: dict[str, Any] | None = None
    """Specification of overall ``matplotlib`` style."""

    save: PlotSave | None = None
    """Arguments for saving the plotted figure into files."""
