from pydantic import BaseModel, Field
from typing import Sequence
from .metadata import Metadata
from .step import Steps
from .stepdefaults import StepDefaults
from .filetype import (  # noqa: F401
    ExtractorFactory as ExtractorFactory,
    FileType as FileType,
)


class DataSchema(BaseModel, extra="forbid"):
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
