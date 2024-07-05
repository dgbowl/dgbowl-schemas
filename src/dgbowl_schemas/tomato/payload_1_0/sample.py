from pydantic import BaseModel


class Sample(BaseModel, extra="allow"):
    """
    Additional attributes for each :class:`Sample` may be required, depending on the
    :class:`Method` type.
    """

    name: str
    """sample name for matching with tomato *pipelines*"""
