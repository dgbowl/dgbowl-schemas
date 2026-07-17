import logging
from pydantic import BaseModel
from typing import Sequence, Literal
from .step import Steps
from ..dataschema_5_1 import DataSchema as NewDataSchema

logger = logging.getLogger(__name__)


class DataSchema(BaseModel, extra="forbid"):
    """
    A :class:`pydantic.BaseModel` implementing ``DataSchema-3.1`` model
    introduced in ``yadg-7.0``.
    """

    version: Literal["3.1"]

    steps: Sequence[Steps]
    """Input commands for :mod:`yadg`'s extractors, organised as a :class:`Sequence`
    of :class:`Steps`."""

    def update(self):
        logger.info("Updating from DataSchema-3.1 to DataSchema-5.1")
        nsch = self.model_dump(exclude_none=True, exclude_defaults=True)
        print(f"{nsch=}")
        nsch["version"] = "5.1"
        for si, s in enumerate(nsch["steps"]):
            step = {"input": s["input"], "tag": s.get("export", None), "extractor": {}}
            if s["datagram"] == "meascsv":
                step["extractor"] = {"filetype": "fhimcpt.csv"}
            elif s["datagram"] == "gctrace":
                step["extractor"] = {"filetype": "ezchrom.asc"}
            elif s["datagram"] == "qftrace":
                step["extractor"] = {"filetype": "fhimcpt.vna"}
            nsch["steps"][si] = step
        nsch["metadata"] = {
            "provenance": {
                "metadata": {"updated-using": "dgbowl-schemas", "from": "3.1"}
            }
        }

        print(f"{nsch=}")
        return NewDataSchema(**nsch)
