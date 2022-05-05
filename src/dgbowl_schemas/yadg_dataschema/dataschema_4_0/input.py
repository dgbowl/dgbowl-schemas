from pydantic import BaseModel, Extra, root_validator
from typing import Optional, Sequence
import os


class Input(BaseModel, extra=Extra.forbid):
    files: Optional[Sequence[str]]
    folders: Optional[Sequence[str]]
    prefix: Optional[str]
    suffix: Optional[str]
    contains: Optional[str]
    exclude: Optional[str]
    encoding: Optional[str] = "UTF-8"

    @root_validator
    def files_or_folders(cls, values):
        assert values.get("files") is not None or values.get("folders") is not None
        assert values.get("files") is None or values.get("folders") is None
        return values

    def paths(self) -> list[str]:
        ret = []
        if self.files is not None:
            paths = self.files
        elif self.folders is not None:
            paths = []
            for folder in self.folders:
                paths += [os.path.join(folder, fn) for fn in os.listdir(folder)]
        for path in sorted(paths):
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
