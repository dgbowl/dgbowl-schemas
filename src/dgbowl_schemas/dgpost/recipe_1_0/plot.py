from pydantic import BaseModel, Field
from typing import Literal, Sequence, Optional, Tuple, Any, Dict


class SeriesIndex(BaseModel, extra="forbid"):
    from_zero: bool = True
    to_units: Optional[str] = None


class Series(BaseModel, extra="allow"):
    y: str
    x: Optional[str] = None
    kind: Literal["scatter", "line", "errorbar"] = "scatter"
    index: Optional[SeriesIndex] = SeriesIndex()


class AxArgs(BaseModel, extra="allow"):
    cols: Optional[Tuple[int, int]] = None
    rows: Optional[Tuple[int, int]] = None
    series: Sequence[Series]
    methods: Optional[Dict[str, Any]] = None
    legend: bool = False


class PlotSave(BaseModel, extra="allow", populate_by_name=True):
    as_: str = Field(alias="as")
    tight_layout: Optional[Dict[str, Any]] = None


class Plot(BaseModel, extra="forbid"):
    table: str
    ax_args: Sequence[AxArgs]
    fig_args: Optional[Dict[str, Any]] = None
    style: Optional[Dict[str, Any]] = None
    nrows: int = 1
    ncols: int = 1
    save: Optional[PlotSave] = None
