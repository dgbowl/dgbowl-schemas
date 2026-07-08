import logging
from pydantic import BaseModel, Field
from typing import Sequence, Optional, Mapping, Any, Literal
from .step import Step
from .stepdefaults import StepDefaults
from .filetype import (  # noqa: F401
    ExtractorFactory as ExtractorFactory,
    FileType as FileType,
    FileTypes as FileTypes,
)
from ..dataschema_7_0 import DataSchema as NewDataSchema

logger = logging.getLogger(__name__)


class DataSchema(BaseModel, extra="forbid"):
    """
    A :class:`pydantic.BaseModel` implementing ``DataSchema-6.0`` model
    introduced in ``yadg-6.0``.
    """

    version: Literal["6.0"]

    metadata: Optional[Mapping[str, Any]]
    """Input metadata for :mod:`yadg`."""

    step_defaults: StepDefaults = Field(..., default_factory=StepDefaults)
    """Default values for configuration of each :class:`Step`."""

    steps: Sequence[Step]
    """Input commands for :mod:`yadg`'s extractors, organised as a :class:`Sequence`
    of :class:`Steps`."""

    def update(self):
        nsch = self.model_dump(exclude_none=True, exclude_defaults=True)
        print(f"{nsch=}")
        for si, s in enumerate(nsch["steps"]):
            if s["extractor"]["filetype"] == "fusion.zip":
                logger.debug("Converting fusion.zip to fusion.json in step %d", si)
                nsch["steps"][si]["extractor"]["filetype"] = "fusion.json"
        nsch["version"] = "7.0"
        print(f"{nsch=}")
        return NewDataSchema(**nsch)
