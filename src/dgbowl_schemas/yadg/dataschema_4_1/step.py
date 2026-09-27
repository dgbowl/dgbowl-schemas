from collections.abc import Mapping
from typing import Any, Literal

from pydantic import BaseModel, Field

from .externaldate import ExternalDate
from .input import Input
from .parameters import Timestamp, Timestamps, Tol

try:
    from typing import Annotated
except ImportError:
    from typing import Annotated


class Dummy(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="allow"):
        pass

    parser: Literal["dummy"]
    input: Input
    parameters: Params | None = None
    tag: str | None = None
    externaldate: ExternalDate | None = None


class BasicCSV(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        sep: str = ","
        sigma: Mapping[str, Tol] | None = None
        calfile: str | None = None
        timestamp: Timestamps | None = None
        convert: Any | None = None
        units: Mapping[str, str] | None = None

    parser: Literal["basiccsv"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: str | None = None
    externaldate: ExternalDate | None = None


class MeasCSV(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        timestamp: Timestamps = Field(
            Timestamp(timestamp={"index": 0, "format": "%Y-%m-%d-%H-%M-%S"})
        )
        calfile: str | None = None
        convert: Any | None = None

    parser: Literal["meascsv"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: str | None = None
    externaldate: ExternalDate | None = None


class FlowData(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["drycal.csv", "drycal.rtf", "drycal.txt"] = "drycal.csv"
        convert: Any | None = None
        calfile: str | None = None

    parser: Literal["flowdata"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: str | None = None
    externaldate: ExternalDate | None = None


class ElectroChem(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["eclab.mpt", "eclab.mpr", "tomato.json"] = "eclab.mpr"

    class Input(Input):
        encoding: str = "windows-1252"

    parser: Literal["electrochem"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: str | None = None
    externaldate: ExternalDate | None = None


class ChromTrace(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal[
            "ezchrom.asc",
            "fusion.json",
            "fusion.zip",
            "agilent.ch",
            "agilent.dx",
            "agilent.csv",
        ] = "ezchrom.asc"
        calfile: str | None = None
        species: Any | None = None
        detectors: Any | None = None

    parser: Literal["chromtrace"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: str | None = None
    externaldate: ExternalDate | None = None


class MassTrace(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["quadstar.sac"] = "quadstar.sac"

    parser: Literal["masstrace"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: str | None = None
    externaldate: ExternalDate | None = None


class QFTrace(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["labview.csv"] = "labview.csv"
        method: Literal["naive", "lorentz", "kajfez"] = "kajfez"
        height: float = 1.0
        distance: float = 5000.0
        cutoff: float = 0.4
        threshold: float = 1e-6

    parser: Literal["qftrace"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: str | None = None
    externaldate: ExternalDate | None = None


class XPSTrace(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["phi.spe"] = "phi.spe"

    parser: Literal["xpstrace"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: str | None = None
    externaldate: ExternalDate | None = None


class XRDTrace(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal[
            "panalytical.xy",
            "panalytical.csv",
            "panalytical.xrdml",
        ] = "panalytical.csv"

    parser: Literal["xrdtrace"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: str | None = None
    externaldate: ExternalDate | None = None


Steps = Annotated[
    Dummy
    | BasicCSV
    | MeasCSV
    | FlowData
    | ElectroChem
    | ChromTrace
    | MassTrace
    | QFTrace
    | XPSTrace
    | XRDTrace,
    Field(discriminator="parser"),
]
