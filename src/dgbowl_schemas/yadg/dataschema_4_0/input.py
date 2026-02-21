from pydantic import BaseModel, model_validator
from typing import Optional, Sequence, List
import os


class Input(BaseModel, extra="forbid"):
    files: Optional[Sequence[str]] = None
    folders: Optional[Sequence[str]] = None
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    contains: Optional[str] = None
    exclude: Optional[str] = None
    encoding: Optional[str] = "UTF-8"

    @model_validator(mode="before")
    def files_or_folders(cls, values):  # pylint: disable=E0213
        if values.get("files") is not None and values.get("folders") is not None:
            raise ValueError("Both 'files' and 'folders' provided.")
        elif values.get("files") is None and values.get("folders") is None:
            raise ValueError("Neither 'files' nor 'folders' provided.")
        return values

    def paths(self) -> List[str]:
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
