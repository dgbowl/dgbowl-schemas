from pydantic import BaseModel
from typing import Literal

class Save(BaseModel):
    class Config:
        allow_population_by_field_name = True
        extra = "forbid"
        fields = {
            'as_': 'as'
        }
    table: str
    as_: str
    type: Literal["pkl", "json", "xlsx", "csv"] = None
    sigma: bool = True

    

