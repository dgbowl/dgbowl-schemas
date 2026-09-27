from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal

from pydantic import BaseModel


class Metadata(BaseModel, extra="forbid"):
    class Provenance(BaseModel, extra="forbid"):
        type: str
        metadata: Mapping[str, Any] | None = None

    provenance: Provenance
    version: Literal["4.1", "4.1.0", "4.1.1", "4.1.2", "4.1.3"]
    timezone: str = "localtime"
