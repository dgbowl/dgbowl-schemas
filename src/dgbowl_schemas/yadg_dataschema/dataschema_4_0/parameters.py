from pydantic import BaseModel, Extra, Field
from typing import Literal, Optional, Union, Any, Mapping

from .timestamp import Timestamp, TimeDate, UTS


class Dummy(BaseModel, extra=Extra.allow):
    parser: Literal["dummy"]


class BasicCSV(BaseModel, extra=Extra.forbid):
    class Tol(BaseModel, extra=Extra.forbid):
        atol: Optional[float]
        rtol: Optional[float]

    parser: Literal["basiccsv"]
    sep: str = ","
    sigma: Optional[Mapping[str, Tol]]
    calfile: Optional[str]
    timestamp: Optional[Union[Timestamp, UTS, TimeDate]]
    convert: Optional[Any]
    units: Optional[Mapping[str, str]]


class MeasCSV(BaseModel, extra=Extra.forbid):
    parser: Literal["meascsv"]
    calfile: Optional[str]
    convert: Optional[Any]


class XPSTrace(BaseModel, extra=Extra.forbid, allow_population_by_field_name=True):
    parser: Literal["xpstrace"]
    filetype: Literal["phi.spe"] = Field("phi.spe", alias="tracetype")


class ChromTrace(BaseModel, extra=Extra.forbid, allow_population_by_field_name=True):
    parser: Literal["chromtrace"]
    calfile: Optional[str]
    filetype: Literal[
        "ezchrom.asc",
        "fusion.json",
        "fusion.zip",
        "agilent.ch",
        "agilent.dx",
        "agilent.csv",
    ] = Field("ezchrom.asc", alias="tracetype")
    species: Optional[Any]
    detectors: Optional[Any]


class ElectroChem(BaseModel, extra=Extra.forbid):
    parser: Literal["electrochem"]
    filetype: Literal["eclab.mpt", "eclab.mpr"]


class FlowData(BaseModel, extra=Extra.forbid, allow_population_by_field_name=True):
    parser: Literal["flowdata"] = Field(..., repr=False)
    filetype: Literal["drycal", "drycal.csv", "drycal.rtf", "drycal.txt"] = "drycal"
    convert: Optional[Any]
    calfile: Optional[str]


class MassTrace(BaseModel, extra=Extra.forbid, allow_population_by_field_name=True):
    parser: Literal["masstrace"]
    filetype: Literal["quadstar.sac"] = Field("quadstar.sac", alias="tracetype")


class QFTrace(BaseModel, extra=Extra.forbid, allow_population_by_field_name=True):
    parser: Literal["qftrace"]
    method: Literal["naive", "lorentz", "kajfez"] = "kajfez"
    height: float = 1.0
    distance: float = 5000.0
    cutoff: float = 0.4
    threshold: float = 1e-6
    filetype: Literal["labview.csv"] = Field("labview.csv", alias="tracetype")


Parameters = Union[
    Dummy,
    BasicCSV,
    MeasCSV,
    XPSTrace,
    ChromTrace,
    ElectroChem,
    FlowData,
    MassTrace,
    QFTrace,
]

Parsernames = Literal[
    "dummy",
    "basiccsv",
    "meascsv",
    "xpstrace",
    "chromtrace",
    "electrochem",
    "flowdata",
    "masstrace",
    "qftrace",
]
