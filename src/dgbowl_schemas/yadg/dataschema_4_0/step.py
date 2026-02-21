from pydantic import BaseModel, Field
from typing import Optional, Literal, Mapping, Any, Union
from .externaldate import ExternalDate
from .input import Input
from .parameters import Tol, Timestamps, Timestamp

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


class Dummy(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="allow"):
        pass

    parser: Literal["dummy"]
    input: Input = Field(alias="import")
    parameters: Optional[Params] = None
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None
    export: Optional[str] = None


class BasicCSV(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        sep: str = ","
        sigma: Optional[Mapping[str, Tol]] = None
        calfile: Optional[str] = None
        timestamp: Optional[Timestamps] = None
        convert: Optional[Any] = None
        units: Optional[Mapping[str, str]] = None

    parser: Literal["basiccsv"]
    input: Input = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None
    export: Optional[str] = None


class MeasCSV(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        timestamp: Timestamps = Field(
            Timestamp(timestamp={"index": 0, "format": "%Y-%m-%d-%H-%M-%S"})
        )
        calfile: Optional[str] = None
        convert: Optional[Any] = None

    parser: Literal["meascsv"]
    input: Input = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None
    export: Optional[str] = None


class FlowData(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["drycal", "drycal.csv", "drycal.rtf", "drycal.txt"] = "drycal"
        convert: Optional[Any] = None
        calfile: Optional[str] = None

    parser: Literal["flowdata"]
    input: Input = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None
    export: Optional[str] = None


class ElectroChem(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["eclab.mpt", "eclab.mpr"] = "eclab.mpr"

    class ECInput(Input):
        encoding: str = "windows-1252"

    parser: Literal["electrochem"]
    input: ECInput = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None
    export: Optional[str] = None


class ChromTrace(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal[
            "ezchrom.asc",
            "fusion.json",
            "fusion.zip",
            "agilent.ch",
            "agilent.dx",
            "agilent.csv",
        ] = Field("ezchrom.asc", alias="tracetype")
        calfile: Optional[str] = None
        species: Optional[Any] = None
        detectors: Optional[Any] = None

    parser: Literal["chromtrace"]
    input: Input = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None
    export: Optional[str] = None


class MassTrace(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["quadstar.sac"] = Field("quadstar.sac", alias="tracetype")

    parser: Literal["masstrace"]
    input: Input = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None
    export: Optional[str] = None


class QFTrace(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["labview.csv"] = Field("labview.csv", alias="tracetype")
        method: Literal["naive", "lorentz", "kajfez"] = "kajfez"
        height: float = 1.0
        distance: float = 5000.0
        cutoff: float = 0.4
        threshold: float = 1e-6

    parser: Literal["qftrace"]
    input: Input = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None
    export: Optional[str] = None


class XPSTrace(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        filetype: Literal["phi.spe"] = Field("phi.spe", alias="tracetype")

    parser: Literal["xpstrace"]
    input: Input = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    tag: Optional[str] = None
    externaldate: Optional[ExternalDate] = None
    export: Optional[str] = None


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
    ],
    Field(discriminator="parser"),
]
