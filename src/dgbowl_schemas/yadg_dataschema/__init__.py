from pydantic import parse_obj_as
from typing import Union
from .dataschema_4_1 import DataSchema as DataSchema_4_1
from .dataschema_4_0 import DataSchema as DataSchema_4_0

def dataschema(**kwargs):
    DataSchema = Union[DataSchema_4_1, DataSchema_4_0]
    return parse_obj_as(DataSchema, kwargs)
