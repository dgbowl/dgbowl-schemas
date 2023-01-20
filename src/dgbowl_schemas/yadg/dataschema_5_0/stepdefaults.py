from pydantic import BaseModel, Extra


class StepDefaults(BaseModel, extra=Extra.forbid):
    """Configuration of defaults applicable for all steps."""

    timezone: str = "localtime"
    """Global timezone specification.

    .. note::

        This should be set to the timezone where the measurements have been
        performed, as opposed to the timezone where ``yadg`` is being executed.
        Otherwise timezone offsets may not be accounted for correctly.

    """

    locale: str = "en_GB.UTF-8"
    """Global locale specification."""

    encoding: str = "UTF-8"
    """Global filetype encoding."""
