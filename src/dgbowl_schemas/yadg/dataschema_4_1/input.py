import os
from collections.abc import Sequence

from pydantic import BaseModel, Field


class Input(BaseModel, extra="forbid", populate_by_name=True):
    files: Sequence[str] = Field(alias="folders")
    prefix: str | None = None
    suffix: str | None = None
    contains: str | None = None
    exclude: str | None = None
    encoding: str = "UTF-8"

    def paths(self) -> list[str]:
        ret = []
        for item in sorted(self.files):
            if os.path.isdir(item):
                paths = [os.path.join(item, fn) for fn in sorted(os.listdir(item))]
            else:
                paths = [item]
            for path in paths:
                tail = os.path.basename(path)
                inc = True
                if self.prefix is not None and not tail.startswith(self.prefix):
                    inc = False
                if self.suffix is not None and not tail.endswith(self.suffix):
                    inc = False
                if self.contains is not None and self.contains not in tail:
                    inc = False
                if self.exclude is not None and self.exclude in tail:
                    inc = False
                if inc:
                    ret.append(path)
        return ret
