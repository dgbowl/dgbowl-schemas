from pydantic import BaseModel
from typing import Optional, Literal, Sequence
from .load import Load
from .extract import Extract
from .transform import Transform
from .save import Save

class RecipeSchema(BaseModel):
    version: Literal["v1.0"]
    load: Sequence[Load]
    extract: Optional[Sequence[Extract]]
    transform: Optional[Sequence[Transform]]
    save: Optional[Sequence[Save]]

def recipe_parser(recipe: dict) -> dict:
    ret = RecipeSchema(**recipe)
    return ret.dict(by_alias=True, exclude_none=True)
