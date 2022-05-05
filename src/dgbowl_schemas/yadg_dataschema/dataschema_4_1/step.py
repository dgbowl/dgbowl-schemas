from pydantic import BaseModel, Extra, Field, root_validator
from typing import Optional
from .parameters import Parameters
from .externaldate import ExternalDate
from .input import Input


class Step(BaseModel, extra=Extra.forbid):
    input: Input
    tag: str = None
    parameters: Parameters = Field(discriminator="parser")
    externaldate: Optional[ExternalDate]
