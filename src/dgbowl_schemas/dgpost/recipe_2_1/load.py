from pydantic import BaseModel, Extra, Field, validator
from typing import Literal, Optional
import logging

logger = logging.getLogger(__name__)


class Load(BaseModel, extra=Extra.forbid, allow_population_by_field_name=True):
    as_: str = Field(alias="as")
    path: str
    type: Literal["datagram", "table"] = "datagram"
    check: Optional[bool] = None

    @validator("check")
    def check_is_deprecated(cls, v):
        if isinstance(v, bool):
            logger.warning("Recipe->Load->check has been deprecated in Recipe-2.1.")
            return None
        else:
            return v
