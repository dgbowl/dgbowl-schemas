from pydantic import BaseModel, Extra, PrivateAttr, Field, root_validator, validator
from typing import Literal, Optional, Union
import logging

logger = logging.getLogger(__name__)


class ExternalDateFile(BaseModel, extra=Extra.forbid):
    class Content(BaseModel, extra=Extra.forbid):
        path: str
        type: str
        match: Optional[str]

    file: Content


class ExternalDateFilename(BaseModel, extra=Extra.forbid):
    class Content(BaseModel, extra=Extra.forbid):
        format: str
        len: int

    filename: Content


class ExternalDateISOString(BaseModel, extra=Extra.forbid):
    isostring: str


class ExternalDateUTSOffset(BaseModel, extra=Extra.forbid):
    utsoffset: float


class ExternalDate(BaseModel, extra=Extra.forbid):
    using: Union[
        ExternalDateFile,
        ExternalDateFilename,
        ExternalDateISOString,
        ExternalDateUTSOffset,
    ]
    mode: Literal["add", "replace"] = "add"
    _default: bool = PrivateAttr()

    def __init__(self, **data):
        self._default = False
        super().__init__(**data)

    @root_validator(pre=True, allow_reuse=True)
    def check_using(cls, values):
        using = values.pop("using", None)
        if using is None and "from" in values:
            logger.warning(
                "Specifying 'from' for ExternalDate was deprecated in "
                "dgbowl_schemas-v103, and may stop working in future "
                "versions of DataSchema. Please use 'using' instead."
            )
            using = values.pop("from")
        if using is None:
            using = {"filename": {"format": "%Y-%m-%d-%H-%M-%S", "len": 19}}
            cls._default = True
        values["using"] = using
        return values
