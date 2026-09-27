import inspect
import logging
import sys
from abc import ABC
from collections.abc import Mapping
from typing import Any, Literal, TypeVar

import tzlocal
from babel import Locale
from pydantic import BaseModel, Field, field_validator

from .parameters import Timestamp, Timestamps
from .stepdefaults import StepDefaults

logger = logging.getLogger(__name__)


class FileType(BaseModel, ABC, extra="forbid"):
    """Template abstract base class for parser classes."""

    filetype: str | None = None
    timezone: str | None = None
    locale: str | None = None
    encoding: str | None = None
    parameters: Any | None = None
    suffix: tuple[str] | None = None

    @field_validator("timezone")
    @classmethod
    def timezone_resolve_localtime(cls, v):
        if v == "localtime":
            v = tzlocal.get_localzone_name()
        return v

    @field_validator("locale")
    @classmethod
    def locale_validate_default(cls, v):
        if v is not None:
            v = str(Locale.parse(v))
        return v


class Example(FileType):
    class Parameters(BaseModel, extra="allow"):
        pass

    parameters: Parameters = Field(default_factory=Parameters)
    filetype: Literal["example"]


class Agilent_ch(FileType):
    filetype: Literal["agilent.ch"]
    suffix: list[str] = [".ch"]


class Agilent_dx(FileType):
    filetype: Literal["agilent.dx"]
    suffix: list[str] = [".dx"]


class Agilent_csv(FileType):
    filetype: Literal["agilent.csv"]
    suffix: list[str] = [".csv"]


class Basic_csv(FileType):
    class Parameters(BaseModel, extra="forbid"):
        sep: str = ","
        """Separator of table columns."""

        strip: str | None = None
        """A :class:`str` of characters to strip from headers & data."""

        units: Mapping[str, str] | None = None
        """A :class:`dict` containing ``column: unit`` keypairs."""

        timestamp: Timestamps | None = None
        """Timestamp specification allowing calculation of Unix timestamp for
        each table row."""

    parameters: Parameters = Field(default_factory=Parameters)
    filetype: Literal["basic.csv"]
    suffix: list[str] = [".csv"]


class Drycal_csv(FileType):
    filetype: Literal["drycal.csv"]
    suffix: list[str] = [".csv"]


class Drycal_rtf(FileType):
    filetype: Literal["drycal.rtf"]
    suffix: list[str] = [".rtf"]


class Drycal_txt(FileType):
    filetype: Literal["drycal.txt"]
    suffix: list[str] = [".txt"]


class EClab_mpr(FileType):
    filetype: Literal["eclab.mpr"]
    suffix: list[str] = [".mpr"]


class EClab_mpt(FileType):
    filetype: Literal["eclab.mpt"]
    encoding: str = "windows-1252"
    suffix: list[str] = [".mpt"]

    @field_validator("encoding")
    @classmethod
    def set_encoding(cls, encoding):
        return encoding or "windows-1252"


class EmpaLC_csv(FileType):
    filetype: Literal["empalc.csv"]
    suffix: list[str] = [".csv"]


class EmpaLC_xlsx(FileType):
    filetype: Literal["empalc.xlsx"]
    suffix: list[str] = [".xlsx"]


class EZChrom_dat(FileType):
    filetype: Literal["ezchrom.dat"]
    suffix: list[str] = [".dat"]


class EZChrom_asc(FileType):
    filetype: Literal["ezchrom.asc"]
    encoding: str = "windows-1252"
    suffix: list[str] = [".dat.asc"]

    @field_validator("encoding")
    @classmethod
    def set_encoding(cls, encoding):
        return encoding or "windows-1252"


class FHI_csv(FileType):
    class Parameters(BaseModel, extra="forbid"):
        timestamp: Timestamps = Field(
            Timestamp(timestamp={"index": 0, "format": "%Y-%m-%d-%H-%M-%S"})
        )

    parameters: Parameters = Field(default_factory=Parameters)
    filetype: Literal["fhimcpt.csv"]
    suffix: list[str] = [".csv"]


class FHI_vna(FileType):
    filetype: Literal["fhimcpt.vna"]
    suffix: list[str] = [".csv"]


class Fusion_json(FileType):
    filetype: Literal["fusion.json", "fusion.zip"]
    suffix: list[str] = [".fusion-data"]

    @field_validator("filetype")
    @classmethod
    def set_encoding(cls, value):
        if value == "fusion.zip":
            logger.warning(
                "Use of 'fusion.zip' filetype has been deprecated in "
                "DataSchema-7.0. Please use 'fusion.json' instead."
            )
            return "fusion.json"
        return value


class Fusion_csv(FileType):
    filetype: Literal["fusion.csv"]
    suffix: list[str] = [".csv"]


class Panalytical_xy(FileType):
    filetype: Literal["panalytical.xy"]
    suffix: list[str] = [".xy"]


class Panalytical_csv(FileType):
    filetype: Literal["panalytical.csv"]
    suffix: list[str] = [".csv"]


class PicoLog_tc08(FileType):
    filetype: Literal["picolog.tc08"]
    suffix: list[str] = [".picolog"]


class Panalytical_xrdml(FileType):
    filetype: Literal["panalytical.xrdml"]
    suffix: list[str] = [".xrdml"]


class Phi_spe(FileType):
    filetype: Literal["phi.spe"]
    suffix: list[str] = [".spe"]


class Quadstar_sac(FileType):
    filetype: Literal["quadstar.sac"]
    suffix: list[str] = [".sac"]


class Tomato_json(FileType):
    filetype: Literal["tomato.json"]
    suffix: list[str] = [".json"]


class Touchstone_snp(FileType):
    filetype: Literal["touchstone.snp"]
    suffix: list[str] = [".s1p", ".s2p"]


class Yadg_json(FileType):
    filetype: Literal["yadg.json"]
    suffix: list[str] = [".json"]


classlist = []
for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj) and issubclass(obj, FileType) and obj is not FileType:
        classlist.append(obj)
FileTypes = TypeVar("FileTypes", *classlist)  # ty: ignore[invalid-legacy-type-variable]


class ExtractorFactory(BaseModel):
    """
    Extractor factory class.

    Given an ``extractor=dict(filetype=k, ...)`` argument, attempts to determine the
    correct :class:`FileType`, parses any additionally supplied parameters for that
    :class:`FileType`, and back-fills defaults such as ``timezone``, ``locale``, and
    ``encoding``.

    The following is the current usage pattern in :mod:`yadg`:

    .. code-block::

        ftype = ExtractorFactory(extractor={"filetype": k}).extractor
    """

    extractor: FileTypes = Field(..., discriminator="filetype")

    @field_validator("extractor")
    @classmethod
    def extractor_set_defaults(cls, v):
        defaults = StepDefaults()
        if v.timezone is None:
            v.timezone = defaults.timezone
        if v.locale is None:
            v.locale = defaults.locale
        if v.encoding is None:
            v.encoding = defaults.encoding
        return v
