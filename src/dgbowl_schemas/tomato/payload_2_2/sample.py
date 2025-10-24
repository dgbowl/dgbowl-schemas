from pydantic import BaseModel


class Sample(BaseModel, extra="allow"):
    """
    Additional attributes for each :class:`Sample` may be required, depending on the
    method within the payload.
    """

    identifier: str
    """
    Sample identifier for matching with tomato *pipelines*. This should be
    the unique sample ID from an ELN/LIMS so that the experimental data can
    be uploaded directly.
    """

    sample_is_parent: bool = True
    """
    Indicates whether the current :class:`Sample` is to be treated as a parent
    :class:`Sample` or not. For :class:`Samples` treated as parent (the default),
    the :class:`Payload` should result in the creation of a child :class:`Sample`,
    i.e. a "destructive experiment" which significantly affects sample state.
    Otherwise, the :class:`Sample` can still be considered to represent the sample
    after the completion of the :class:`Payload`.

    .. note::
       This setting will affect how RO-crates are used to upload the tomato output.
    """