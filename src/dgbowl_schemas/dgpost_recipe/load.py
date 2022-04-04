from pydantic import BaseModel
from typing import Literal


class Load(BaseModel):
    class Config:
        allow_population_by_field_name = True
        extra = "forbid"
        fields = {"as_": "as"}

    as_: str
    path: str
    type: Literal["datagram", "table"] = "datagram"
    check: bool = True
