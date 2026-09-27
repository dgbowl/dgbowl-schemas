from __future__ import annotations

import locale
import logging

import tzlocal
from babel import Locale, UnknownLocaleError
from pydantic import BaseModel, Field, field_validator

logger = logging.getLogger(__name__)


class StepDefaults(BaseModel, extra="forbid"):
    """Configuration of defaults applicable for all steps."""

    timezone: str = Field("localtime", validate_default=True)
    """Global timezone specification.

    .. note::

        This should be set to the timezone where the measurements have been
        performed, as opposed to the timezone where :mod:`yadg` is being executed.
        Otherwise timezone offsets may not be accounted for correctly.

    """

    locale: str | None = Field(None, validate_default=True)
    """Global locale specification. Will default to current locale."""

    encoding: str = "utf-8"
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
        if v is not None:
            v = str(Locale.parse(v))
        else:
            for loc in (locale.getlocale(locale.LC_NUMERIC)[0], locale.getlocale()[0]):
                try:
                    v = str(Locale.parse(loc))
                    break
                except (TypeError, UnknownLocaleError, ValueError) as e:
                    logger.debug("Could not process locale '%s': %s", loc, e)
            else:
                logger.debug("No valid locale string provided. Defaulting to 'en_GB'.")
                v = "en_GB"
        return v
