from pydantic.v1 import BaseModel, Extra, Field
from typing import Sequence
from .metadata import Metadata
from .step import Steps
from .stepdefaults import StepDefaults
from .filetype import (
    ExtractorFactory as ExtractorFactory,
    FileType as FileType,
)  # noqa: F401


class DataSchema(BaseModel, extra=Extra.forbid):
    """
    A :class:`pydantic.BaseModel` implementing ``DataSchema-5.0`` model introduced in
    ``yadg-5.0``.
    """

    metadata: Metadata
    """Input metadata for :mod:`yadg`."""

    step_defaults: StepDefaults = Field(StepDefaults())
    """Default values for configuration of :mod:`yadg`'s parsers."""

    steps: Sequence[Steps]
    """Input commands for :mod:`yadg`'s parsers, organised as a sequence of steps."""
