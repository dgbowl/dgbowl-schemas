from pydantic import BaseModel, Field, field_validator
from typing import Optional
import locale
from babel import Locale, UnknownLocaleError
import tzlocal


class StepDefaults(BaseModel, extra="forbid"):
    """Configuration of defaults applicable for all steps."""

    timezone: str = Field("localtime", validate_default=True)
    """Global timezone specification.

    .. note::

        This should be set to the timezone where the measurements have been
        performed, as opposed to the timezone where :mod:`yadg` is being executed.
        Otherwise timezone offsets may not be accounted for correctly.

    """

    locale: Optional[str] = Field(None, validate_default=True)
    """Global locale specification. Will default to current locale."""

    encoding: Optional[str] = "utf-8"
    """Global filetype encoding. Will default to ``utf-8``."""

    @field_validator("timezone")
    @classmethod
    def timezone_resolve_localtime(cls, v):
        if v == "localtime":
            v = tzlocal.get_localzone_name()
        return v

    @field_validator("locale")
    @classmethod
    def locale_set_default(cls, v):
        if v is None:
            v = locale.getlocale(locale.LC_NUMERIC)[0]
        try:
            v = str(Locale.parse(v))
        except (TypeError, UnknownLocaleError):
            v = "en_GB"
        return v
