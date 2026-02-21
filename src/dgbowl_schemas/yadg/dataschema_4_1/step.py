from pydantic import BaseModel, Field
from typing import Optional, Literal, Mapping, Any, Union
from .externaldate import ExternalDate
from .input import Input
from .parameters import Tol, Timestamps, Timestamp

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


class Dummy(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="allow"):
        pass

    parser: Literal["dummy"]
    input: Input
    parameters: Optional[Params] = None
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None


class BasicCSV(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        sep: str = ","
        sigma: Optional[Mapping[str, Tol]] = None
        calfile: Optional[str] = None
        timestamp: Optional[Timestamps] = None
        convert: Optional[Any] = None
        units: Optional[Mapping[str, str]] = None

    parser: Literal["basiccsv"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None


class MeasCSV(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        timestamp: Timestamps = Field(
            Timestamp(timestamp={"index": 0, "format": "%Y-%m-%d-%H-%M-%S"})
        )
        calfile: Optional[str] = None
        convert: Optional[Any] = None

    parser: Literal["meascsv"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None


class FlowData(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["drycal.csv", "drycal.rtf", "drycal.txt"] = "drycal.csv"
        convert: Optional[Any] = None
        calfile: Optional[str] = None

    parser: Literal["flowdata"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None


class ElectroChem(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["eclab.mpt", "eclab.mpr", "tomato.json"] = "eclab.mpr"

    class Input(Input):
        encoding: str = "windows-1252"

    parser: Literal["electrochem"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None


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
        calfile: Optional[str] = None
        species: Optional[Any] = None
        detectors: Optional[Any] = None

    parser: Literal["chromtrace"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None


class MassTrace(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["quadstar.sac"] = "quadstar.sac"

    parser: Literal["masstrace"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None


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
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None


class XPSTrace(BaseModel, extra="forbid"):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["phi.spe"] = "phi.spe"

    parser: Literal["xpstrace"]
    input: Input
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None


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
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None


Steps = Annotated[
    Union[
        Dummy,
        BasicCSV,
        MeasCSV,
        FlowData,
        ElectroChem,
        ChromTrace,
        MassTrace,
        QFTrace,
        XPSTrace,
        XRDTrace,
    ],
    Field(discriminator="parser"),
]
