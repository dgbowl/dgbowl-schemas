from __future__ import annotations

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
    table: str
    ax_args: Sequence[AxArgs]
    fig_args: dict[str, Any] | None = None
    style: dict[str, Any] | None = None
    nrows: int = 1
    ncols: int = 1
    save: PlotSave | None = None
