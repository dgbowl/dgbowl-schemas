from pydantic import BaseModel, Extra, Field, root_validator
from typing import Literal, Union, Sequence
import json
import yaml

from .sample import BatterySample, Sample
from .biologic import BiologicPayloads

class Payload(BaseModel, extra = Extra.forbid):
    version: Literal["0.1"]
    sample: Union[
        BatterySample, 
        Sample
    ] = Field(..., discriminator = "type")
    payload: Sequence[
        BiologicPayloads, 
        DummyPayloads
    ] = Field(..., discriminator = "name")

    @root_validator(pre=True)
    def check_for_files(cls, values):
        for key in ["sample", "payload"]:
            exclusive = {key, f"{key}file"}
            assert len(exclusive.intersection(values)) == 1, (
                "multiple keys provided: " f"{exclusive.intersection(values)}"
            )
            if key in values:
                continue
            else:
                fn = values.pop(f"{key}file")
                with open(fn, "r") as infile:
                    if fn.endswith("json"):
                        data = json.load(infile)
                    elif fn.endswith("yml") or fn.endswith("yaml"):
                        data = yaml.safe_load(infile)
                values[key] = data
        return values
