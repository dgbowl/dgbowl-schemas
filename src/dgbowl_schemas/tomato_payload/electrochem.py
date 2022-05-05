from pydantic import BaseModel, Extra
from typing import Literal, Union

class OpenCircuitVoltage(BaseModel, extra = Extra.forbid):
    name: Literal["open_circuit_voltage"]

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

ElectroChemPayloads = Union[
    OpenCircuitVoltage,
    ConstantCurrent,
    ConstantVoltage,
    SweepCurrent,
    SweepVoltage,
    Loop,
]