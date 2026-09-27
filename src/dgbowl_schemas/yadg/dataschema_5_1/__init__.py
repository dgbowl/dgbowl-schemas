from collections.abc import Mapping, Sequence
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field

from ..dataschema_6_0 import DataSchema as NewDataSchema
from .filetype import (
    ExtractorFactory as ExtractorFactory,
)
from .filetype import (
    FileType as FileType,
)
from .filetype import (
    FileTypes as FileTypes,
)
from .step import Step
from .stepdefaults import StepDefaults


class DataSchema(BaseModel, extra="forbid"):
    """
    A :class:`pydantic.BaseModel` implementing ``DataSchema-5.1`` model
    introduced in ``yadg-5.1``.
    """

    version: Literal["5.1"]

    metadata: Optional[Mapping[str, Any]]
    """Input metadata for :mod:`yadg`."""

    step_defaults: StepDefaults = Field(..., default_factory=StepDefaults)
    """Default values for configuration of each :class:`Step`."""

    steps: Sequence[Step]
    """Input commands for :mod:`yadg`'s extractors, organised as a :class:`Sequence`
    of :class:`Steps`."""

    def update(self):
        nsch = self.model_dump(exclude_none=True, exclude_defaults=True)

        nsch["version"] = "6.0"
        return NewDataSchema(**nsch)
