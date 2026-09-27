from collections.abc import Mapping
from typing import Any, Literal

from pydantic import BaseModel


class Metadata(BaseModel, extra="forbid"):
    """
    The :class:`Metadata` is a container for any metadata of the :class:`DataSchema`.

    """

    class Provenance(BaseModel, extra="forbid"):
        type: str
        """Provenance type. Common values include ``'manual'`` etc."""

        metadata: Mapping[str, Any] | None = None
        """Detailed provenance metadata in a free-form :class:`dict`."""

    version: Literal["5.0"]

    provenance: Provenance
