from pydantic import BaseModel, Extra, Field, root_validator
from typing import Literal, Optional, Union, Any, Mapping
import logging

from .timestamp import Timestamp, TimeDate, UTS

logger = logging.getLogger(__name__)


class Tol(BaseModel, extra=Extra.forbid):
    atol: Optional[float]
    rtol: Optional[float]


class Dummy(BaseModel, extra=Extra.allow):
    parser: Literal["dummy"]


class BasicCSV(BaseModel, extra=Extra.forbid):
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


class XPSTrace(BaseModel, extra=Extra.forbid):
    parser: Literal["xpstrace"]
    filetype: Literal["phi.spe"] = "phi.spe"

    @root_validator(pre=True, allow_reuse=True)
    def check_tracetype(cls, values):
        input = values.get("filetype")
        if input is None and "tracetype" in values:
            logger.warning(
                "Specifying 'tracetype' for XPSTrace was deprecated in "
                "dgbowl_schemas-v103, and may stop working in future versions "
                "of DataSchema. Please use 'filetype' instead."
            )
            input = values.pop("tracetype")
            values["filetype"] = input
        return values


class XRDTrace(BaseModel, extra=Extra.forbid):
    parser: Literal["xrdtrace"]
    filetype: Literal["panalytical.xy", "panalytical.csv", "panalytical.rdxml"]

    @root_validator(pre=True, allow_reuse=True)
    def check_tracetype(cls, values):
        input = values.get("filetype")
        if input is None and "tracetype" in values:
            logger.warning(
                "Specifying 'tracetype' for XRDTrace was deprecated in "
                "dgbowl_schemas-v103, and may stop working in future versions "
                "of DataSchema. Please use 'filetype' instead."
            )
            input = values.pop("tracetype")
            values["filetype"] = input
        return values


class ChromTrace(BaseModel, extra=Extra.forbid):
    parser: Literal["chromtrace"]
    calfile: Optional[str]
    filetype: Literal[
        "ezchrom.asc",
        "fusion.json",
        "fusion.zip",
        "agilent.ch",
        "agilent.dx",
        "agilent.csv",
    ] = "ezchrom.asc"
    species: Optional[Any]
    detectors: Optional[Any]

    @root_validator(pre=True, allow_reuse=True)
    def check_tracetype(cls, values):
        input = values.get("filetype")
        if input is None and "tracetype" in values:
            logger.warning(
                "Specifying 'tracetype' for ChromTrace was deprecated in "
                "dgbowl_schemas-v103, and may stop working in future versions "
                "of DataSchema. Please use 'filetype' instead."
            )
            input = values.pop("tracetype")
            values["filetype"] = input
        return values


class ElectroChem(BaseModel, extra=Extra.forbid):
    parser: Literal["electrochem"]
    filetype: Literal["eclab.mpt", "eclab.mpr"]


class FlowData(BaseModel, extra=Extra.forbid):
    parser: Literal["flowdata"] = Field(..., repr=False)
    filetype: Literal["drycal.csv", "drycal.rtf", "drycal.txt"]
    convert: Optional[Any]
    calfile: Optional[str]


class MassTrace(BaseModel, extra=Extra.forbid):
    parser: Literal["masstrace"]
    filetype: Literal["quadstar.sac"] = "quadstar.sac"

    @root_validator(pre=True, allow_reuse=True)
    def check_tracetype(cls, values):
        input = values.get("filetype")
        if input is None and "tracetype" in values:
            logger.warning(
                "Specifying 'tracetype' for MassTrace was deprecated in "
                "dgbowl_schemas-v103, and may stop working in future versions "
                "of DataSchema. Please use 'filetype' instead."
            )
            input = values.pop("tracetype")
            values["filetype"] = input
        return values


class QFTrace(BaseModel, extra=Extra.forbid):
    parser: Literal["qftrace"]
    method: Literal["naive", "lorentz", "kajfez"] = "kajfez"
    height: float = 1.0
    distance: float = 5000.0
    cutoff: float = 0.4
    threshold: float = 1e-6
    filetype: Literal["labview.csv"] = "labview.csv"

    @root_validator(pre=True, allow_reuse=True)
    def check_tracetype(cls, values):
        input = values.get("filetype")
        if input is None and "tracetype" in values:
            logger.warning(
                "Specifying 'tracetype' for QFTrace was deprecated in "
                "dgbowl_schemas-v103, and may stop working in future versions "
                "of DataSchema. Please use 'filetype' instead."
            )
            input = values.pop("tracetype")
            values["filetype"] = input
        return values
