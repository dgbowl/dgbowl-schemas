from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

from pydantic import BaseModel, Field


class Save(BaseModel, extra="forbid", populate_by_name=True):
    """Save a table into an external (``pkl``, ``xlsx``) file."""

    table: str
    """The name of the table loaded in memory to be stored."""

    as_: str = Field(alias="as")
    """Path to which the table is stored."""

    type: Literal["pkl", "json", "xlsx", "csv", "nc"] | None = None
    """
    Type of the output file.

    .. note::

        Round-tripping of :mod:`dgpost` data is only possible using the ``pkl`` and ``nc``
        formats. For long-term storage, the ``json`` and ``nc`` formats may be better suited.
        The other formats (``xlsx`` and ``csv``) are provided for convenience only and should
        not be used for chaining of :mod:`dgpost` runs.
    """

    columns: Sequence[str] | None = None
    """
    Columns to be exported. By default (``None``), all columns from the specified ``table``
    will be exported.

    .. note::

       If any of the columns supplied is not present in the table, a warning will be
       printed by :mod:`dgpost`.

    """

    sigma: bool = True
    """Whether uncertainties/error estimates in the data should be stripped. Particularly
    useful when exporting into ``xlsx`` or ``csv``."""
