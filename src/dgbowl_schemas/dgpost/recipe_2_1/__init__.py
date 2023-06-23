from pydantic import BaseModel, Extra
from typing import Optional, Literal, Sequence
from .load import Load
from .extract import Extract
from .pivot import Pivot
from .transform import Transform
from .plot import Plot
from .save import Save


class Recipe(BaseModel, extra=Extra.forbid):
    version: Literal["2.1"]
    load: Optional[Sequence[Load]]
    extract: Optional[Sequence[Extract]]
    pivot: Optional[Sequence[Pivot]]
    transform: Optional[Sequence[Transform]]
    plot: Optional[Sequence[Plot]]
    save: Optional[Sequence[Save]]
