from __future__ import annotations

from typing import Literal, Union

from pydantic import BaseModel, Field

from .input import Input

try:
    from typing import Annotated
except ImportError:
    from typing import Annotated


class MeasCSV(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        Tcalfile: str | None = None
        MFCcalfile: str | None = None

    datagram: Literal["meascsv"]
    input: Input = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    export: str | None = None


class QFTrace(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        method: Literal["naive", "lorentz", "kajfez", "q0refl"] = "kajfez"
        cutoff: float = 0.4

    datagram: Literal["qftrace"]
    input: Input = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    export: str | None = None


class GCTrace(BaseModel, extra="forbid", populate_by_name=True):
    class Params(BaseModel, extra="forbid"):
        calfile: str | None = None

    datagram: Literal["gctrace"]
    input: Input = Field(alias="import")
    parameters: Params = Field(default_factory=Params)
    export: str | None = None


Steps = Annotated[
    Union[
        MeasCSV,
        QFTrace,
        GCTrace,
    ],
    Field(discriminator="datagram"),
]
