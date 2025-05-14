from pydantic import BaseModel, Field
from typing import Optional, Any, Dict


class Task(BaseModel, extra="forbid"):
    """
    The :class:`Task` is a driver/device-independent abstraction describing the
    measurement steps. The driver-specific information for the :class:`Task` can be
    provided via the :obj:`technique_name` and :obj:`task_params` parameters.
    """

    component_role: str
    """role of the pipeline *component* on which this :class:`Task` should run"""

    max_duration: float
    """the maximum duration of this :class:`Task`, in seconds"""

    sampling_interval: float
    """the interval between measurements, in seconds"""

    polling_interval: Optional[float] = None
    """
    the interval between polling for data by the ``tomato-job`` process, in seconds;
    defaults to the value in driver settings
    """

    technique_name: str
    """
    the name of the technique; has to match one of the capabilities of the *component*
    on which this :class:`Task` will be executed
    """

    task_name: Optional[str] = None
    """
    the (optional) name of the current :class:`Task`; can be used for triggering other
    :class:`Task` in parallel to this one via :obj:`start_with_task_name`
    """

    task_params: Optional[Dict[str, Any]] = Field(default_factory=dict)
    """
    a :class:`dict` of any additional parameters required to specify the experimental
    technique; the key-value pairs of this :class:`dict` will be used as attr-val
    pairs by the :func:`set_attr` method of the *component* executing this :class:`Task`
    """

    start_with_task_name: Optional[str] = None
    """
    the :obj:`task_name` of the :class:`Task` that this :class:`Task` should be
    started in parallel with; when set, this :class:`Task` will wait for execution until
    a :class:`Task` with the matching :obj:`task_name` is started
    """
