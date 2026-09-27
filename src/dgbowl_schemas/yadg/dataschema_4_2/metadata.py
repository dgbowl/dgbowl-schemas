from collections.abc import Mapping
from typing import Any, Literal

from pydantic import BaseModel


class Metadata(BaseModel, extra="forbid"):
    """Metadata, including version and provenance of the :class:`DataSchema`."""

    class Provenance(BaseModel, extra="forbid"):
        type: str
        metadata: Mapping[str, Any] | None = None

    version: Literal["4.2"]

    provenance: Provenance
    """Provenance information."""

    timezone: str = "localtime"
    """Timezone specification.

    .. note::

        This should be set to the timezone where the measurements have been
        performed, as opposed to the timezone where yadg is being executed,
        otherwise timezone offsets may not be accounted for correctly.

    """
