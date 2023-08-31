from pydantic import BaseModel, Field
from typing import Literal


class Save(BaseModel, extra="forbid", populate_by_name=True):
    """Save a table into an external (``pkl``, ``xlsx``) file."""

    table: str
    """The name of the table loaded in memory to be stored."""

    as_: str = Field(alias="as")
    """Path to which the table is stored."""

    type: Literal["pkl", "json", "xlsx", "csv", "nc"] = None
    """
    Type of the output file.

    .. note::

        Round-tripping of :mod:`dgpost` data is only possible using the ``pkl`` and ``nc``
        formats. For long-term storage, the ``json`` and ``nc`` formats may be better suited.
        The other formats (``xlsx`` and ``csv``) are provided for convenience only and should
        not be used for chaining of :mod:`dgpost` runs.
    """

    sigma: bool = True
    """Whether uncertainties/error estimates in the data should be stripped. Particularly
    useful when exporting into ``xlsx`` or ``csv``."""
