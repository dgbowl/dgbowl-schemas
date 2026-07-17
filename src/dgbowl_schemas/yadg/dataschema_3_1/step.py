from pydantic import BaseModel, Field
from typing import Optional, Literal, Union
from .input import Input

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


class MeasCSV(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        Tcalfile: Optional[str] = None
        MFCcalfile: Optional[str] = None

    datagram: Literal["meascsv"]
    input: Input = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    export: Optional[str] = None


class QFTrace(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        method: Literal["naive", "lorentz", "kajfez", "q0refl"] = "kajfez"
        cutoff: float = 0.4

    datagram: Literal["qftrace"]
    input: Input = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    export: Optional[str] = None


class GCTrace(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        calfile: Optional[str] = None

    datagram: Literal["gctrace"]
    input: Input = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    export: Optional[str] = None


Steps = Annotated[
    Union[
        MeasCSV,
        QFTrace,
        GCTrace,
    ],
    Field(discriminator="datagram"),
]
