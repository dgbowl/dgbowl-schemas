from collections.abc import Mapping, Sequence
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field

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
    A :class:`pydantic.BaseModel` implementing ``DataSchema-7.0`` model
    introduced in ``yadg-7.0``.
    """

    version: Literal["7.0"]

    metadata: Optional[Mapping[str, Any]]
    """Input metadata for :mod:`yadg`."""

    step_defaults: StepDefaults = Field(..., default_factory=StepDefaults)
    """Default values for configuration of each :class:`Step`."""

    steps: Sequence[Step]
    """Input commands for :mod:`yadg`'s extractors, organised as a :class:`Sequence`
    of :class:`Steps`."""
