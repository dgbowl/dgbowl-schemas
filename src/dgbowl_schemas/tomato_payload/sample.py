from pydantic import BaseModel, Extra
from typing import Literal, Mapping

class BatterySample(BaseModel, extra = Extra.forbid):

    class Capacity(BaseModel, extra = Extra.forbid):
        nominal: float
        actual: float

    name: str
    type: Literal["battery"]
    capacity: Capacity


class Sample(BaseModel, extra = Extra.allow):
    name: str
    type: str


    