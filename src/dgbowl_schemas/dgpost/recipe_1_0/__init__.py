import logging
from collections.abc import Sequence
from typing import Literal, Optional

from pydantic import BaseModel

from ..recipe_2_1 import Recipe as NewRecipe
from .extract import Extract
from .load import Load
from .plot import Plot
from .save import Save
from .transform import Transform

logger = logging.getLogger(__name__)


class Recipe(BaseModel, extra="forbid"):
    version: Literal["v1.0", "1.0", "1.1", "2.0"]
    load: Optional[Sequence[Load]] = None
    extract: Optional[Sequence[Extract]] = None
    transform: Optional[Sequence[Transform]] = None
    plot: Optional[Sequence[Plot]] = None
    save: Optional[Sequence[Save]] = None

    def update(self):
        logger.info("Updating from Recipe-1.0 to Recipe-2.1")

        nsch = {"version": "2.1"}
        for k in ("load", "extract", "transform", "plot", "save"):
            attr = getattr(self, k)
            if attr is not None:
                nsch[k] = [i.model_dump(by_alias=True, exclude_none=True) for i in attr]
        return NewRecipe(**nsch)
