from pydantic import BaseModel, Extra, Field, root_validator
from typing import Optional
from .parameters import Parameters, Parsernames
from .externaldate import ExternalDate
from .input import Input


class Step(BaseModel, extra=Extra.forbid):
    parser: Parsernames
    input: Input = Field(alias="import")
    parameters: Parameters = Field(default=None, discriminator="parser")
    tag: Optional[str]
    externaldate: Optional[ExternalDate]
    export: Optional[str]

    @root_validator(pre=True, allow_reuse=True)
    def copy_parser_to_params(cls, values):
        params = values.get("parameters")
        if params is not None:
            values["parameters"]["parser"] = values["parser"]
        return values
