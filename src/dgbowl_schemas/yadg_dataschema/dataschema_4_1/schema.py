from pydantic import BaseModel, Extra
from typing import Sequence
from .metadata import Metadata
from .step import Step


class DataSchema(BaseModel, extra=Extra.forbid):
    metadata: Metadata
    steps: Sequence[Step]
