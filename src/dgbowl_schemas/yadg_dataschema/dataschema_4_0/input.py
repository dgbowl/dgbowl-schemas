from pydantic import BaseModel, Extra, root_validator
from typing import Optional, Sequence
import os


class Input(BaseModel, extra=Extra.forbid):
    files: Sequence[str]
    prefix: Optional[str]
    suffix: Optional[str]
    contains: Optional[str]
    exclude: Optional[str]
    encoding: Optional[str] = "UTF-8"

    @root_validator(pre=True, allow_reuse=True)
    def check_exclusive(cls, values):
        keys = {"files", "folders"}.intersection(set(values))
        if len(keys) > 1:
            raise ValueError(
                f"Specifying multiple arguments ({keys}) to Input is not allowed."
            )
        elif len(keys) == 0:
            raise ValueError(f"Either 'files' or 'folders' must be supplied to Input.")
        if values.get("files") is not None:
            pass
        else:
            folders = values.pop("folders")
            files = []
            for folder in folders:
                files += [os.path.join(folder, file) for file in os.listdir(folder)]
            values["files"] = files
        return values

    def paths(self) -> list[str]:
        ret = []
        for path in sorted(self.files):
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
