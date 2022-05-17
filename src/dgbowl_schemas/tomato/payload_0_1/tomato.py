from pydantic import BaseModel, Extra, Field

class Tomato(BaseModel, extra=Extra.forbid):

    class Output(BaseModel, extra=Extra.forbid):
        path: str = None
        prefix: str = None

    unlock_when_done: bool = False
    output: Output = Field(default_factory=Output)