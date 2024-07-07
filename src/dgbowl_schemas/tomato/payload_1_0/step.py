from pydantic import BaseModel
from typing import Optional, Any


class Step(BaseModel, extra="forbid"):
    """
    The :class:`Step` is a driver/device-independent abstraction describing the
    measurement steps. The driver-specific information for the :class:`Step` can be
    provided via the ``technique`` parameter.
    """

    component_tag: str
    """tag of the pipeline component on which this :class:`Method` should run"""

    max_duration: float
    """the maximum duration of this :class:`Step`, in seconds"""

    sampling_interval: float
    """the interval between measurements, in seconds"""

    polling_interval: Optional[int] = None
    """the interval between polling for data, in seconds; defaults to the value in driver settings"""

    technique: Optional[dict[str, Any]] = None
    """a :class:`dict` of additional parameters required to specify the experimental technique"""
