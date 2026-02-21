from pydantic import BaseModel
from typing import Optional, Literal, Sequence
from .load import Load
from .extract import Extract
from .transform import Transform
from .plot import Plot
from .save import Save
from ..recipe_2_1 import Recipe as NewRecipe
import logging

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
        for k in {"load", "extract", "transform", "plot", "save"}:
            attr = getattr(self, k)
            if attr is not None:
                nsch[k] = [i.model_dump(by_alias=True, exclude_none=True) for i in attr]
        return NewRecipe(**nsch)
