from pydantic import BaseModel
from typing import Optional


class User(BaseModel, extra="allow"):
    """
    Additional attributes for each :class:`Sample` may be required, depending on the
    method within the payload.
    """

    identifier: str
    """
    User identifier for matching annotating the user running this payload. This
    should be the unique ID of the :class:`Person` in an ELN/LIMS so that the
    experimental data can be attributed properly.

    .. note::
       This identifier is used to construct the ``author`` property within the
       RO-crate mechanism.
    """

    api_key: Optional[str] = None
    """
    An API key which allows this :class:`User` to upload tomato results to the
    ELN/LIMS using the RO-crate mechanism.

    .. caution::
       Storing private per-user API keys in payload files is discouraged as
       those files are meant to be shared; provide an appropriately scoped
       API key instead (which can be e.g. whitelisted by the ELN/LIMS based
       on the IP/MAC address of the PC running tomato).
    """