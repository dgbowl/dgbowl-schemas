from pydantic import BaseModel, Extra, Field, root_validator
from typing import Optional
from .parameters import Parameters, Parsernames
from .externaldate import ExternalDate
from .input import Input


class Step(BaseModel, extra=Extra.forbid):
    parser: Parsernames
    input: Input = Field(alias="import")
    parameters: Optional[Parameters]
    tag: Optional[str]
    externaldate: Optional[ExternalDate]
    export: Optional[str]