from collections.abc import Mapping
from typing import Any, Literal, Optional

from pydantic import BaseModel


class Metadata(BaseModel, extra="forbid"):
    """
    The :class:`Metadata` is a container for any metadata of the :class:`DataSchema`.

    """

    class Provenance(BaseModel, extra="forbid"):
        type: str
        """Provenance type. Common values include ``'manual'`` etc."""

        metadata: Optional[Mapping[str, Any]] = None
        """Detailed provenance metadata in a free-form :class:`dict`."""

    version: Literal["5.0"]

    provenance: Provenance
