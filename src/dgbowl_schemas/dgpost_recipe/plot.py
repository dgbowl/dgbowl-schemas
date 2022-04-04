from pydantic import BaseModel
from typing import Literal, Sequence, Optional, Tuple, Any


class SeriesIndex(BaseModel):
    from_zero: bool = True
    to_units: Optional[str]


class Series(BaseModel):
    y: str
    x: Optional[str]
    kind: Literal["scatter", "line", "errorbar"] = "scatter"
    index: Optional[SeriesIndex] = SeriesIndex()


class AxArgs(BaseModel):
    series: Sequence[Series]
    rows: Optional[Tuple[int, int]]
    cols: Optional[Tuple[int, int]]
    legend: bool = False
    methods: Optional[dict[str, Any]]


class PlotSave(BaseModel):
    class Config:
        allow_population_by_field_name = True
        fields = {"as_": "as"}

    as_: str
    tight_layout: Optional[dict[str, Any]]


class Plot(BaseModel):
    class Config:
        extra = "forbid"

    table: str
    ax_args: Sequence[AxArgs]
    fig_args: Optional[dict[str, Any]]
    style: Optional[dict[str, Any]]
    nrows: int = 1
    ncols: int = 1
    save: Optional[PlotSave]
