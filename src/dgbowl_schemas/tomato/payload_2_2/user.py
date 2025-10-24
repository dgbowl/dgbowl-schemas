from pydantic import BaseModel


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
