from pydantic import BaseModel, Extra
from typing import Literal, Union

allowed_I_ranges = Literal[
    "keep", "100 pA", "1 nA", "10 nA", "100 nA", "1 uA", "10 uA", "100 uA",
    "1 mA", "10 mA", "100 mA", "1 A", "booster", "auto",
]
allowed_E_ranges = Literal[
    "+-2.5 V", "+-5.0 V", "+-10 V", "auto",
]

class OpenCircuitVoltage(BaseModel, extra = Extra.forbid):
    name: Literal["open_circuit_voltage"]
    time: float = 0.0
    record_every_dt: float = 30.0
    record_every_dE: float = 0.005
    I_range: allowed_I_ranges = "keep"
    E_range: allowed_E_ranges = "auto"

class ConstantVoltage(BaseModel, extra = Extra.forbid):
    name: Literal["constant_voltage"]

class ConstantCurrent(BaseModel, extra = Extra.forbid):
    name: Literal["constant_current"]

class SweepVoltage(BaseModel, extra = Extra.forbid):
    name: Literal["sweep_voltage"]

class SweepCurrent(BaseModel, extra = Extra.forbid):
    name: Literal["sweep_current"]

class Loop(BaseModel, extra = Extra.forbid):
    name: Literal["loop"]
    n_gotos: int = -1
    goto: int = 0

ElectroChemPayloads = Union[
    OpenCircuitVoltage,
    ConstantCurrent,
    ConstantVoltage,
    SweepCurrent,
    SweepVoltage,
    Loop,
]