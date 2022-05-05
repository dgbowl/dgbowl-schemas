from pydantic import BaseModel, Extra
from typing import Literal, Union

class Random(BaseModel, extra = Extra.forbid):
    name: Literal["random"]
    delay: float = 1.0
    time: float = 10.0

class Sequential(BaseModel, extra = Extra.forbid):
    name: str
    delay: float = 1.0
    time: float = 10.0

DummyPayloads = Union[Random, Sequential]