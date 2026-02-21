from pydantic import BaseModel, Field, model_validator
from typing import Optional, Sequence, Any
import logging

logger = logging.getLogger(__name__)


class At(BaseModel, extra="forbid"):
    steps: Sequence[str] = None
    indices: Sequence[int] = None
    timestamps: Sequence[float] = None

    @model_validator(mode="before")
    def check_one_input(cls, values):  # pylint: disable=E0213
        keys = {"step", "steps", "index", "indices", "timestamp"}
        assert len(keys.intersection(set(values))) == 1, (
            f"multiple keys provided: {keys.intersection(values)}"
        )
        if "step" in values:
            values["steps"] = [values.pop("step")]
        elif "index" in values:
            values["indices"] = [values.pop("index")]
        return values


class Constant(BaseModel, extra="forbid"):
    value: Any
    as_: str = Field(alias="as")
    units: Optional[str] = None


class Column(BaseModel, extra="forbid"):
    key: str
    as_: str = Field(alias="as")


class Extract(BaseModel, extra="forbid", populate_by_name=True):
    into: str
    from_: Optional[str] = Field(None, alias="from")
    at: Optional[At] = None
    constants: Optional[Sequence[Constant]] = None
    columns: Optional[Sequence[Column]] = None

    @model_validator(mode="before")
    def check_one_input(cls, values):  # pylint: disable=E0213
        keys = {"constants", "columns"}
        if len(keys.intersection(set(values))) == 0:
            logging.info("did not provide any of '%s'", keys)
        return values
