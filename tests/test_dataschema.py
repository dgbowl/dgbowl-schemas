import pytest
import os
from pydantic import ValidationError
import json
from dgbowl_schemas.yadg import to_dataschema

from ref_dataschema import ts0, ts1, ts2, ts3, ts4, ts5


@pytest.mark.parametrize(
    "inpath, success",
    [
        ("metadata_ts0.json", True),
        ("metadata_ts1.json", False),
        ("metadata_ts2.json", True),
        ("metadata_ts3.json", False),
        ("metadata_ts4.json", False),
        ("metadata_ts5.json", True),
        ("metadata_ts6.json", False),
        ("metadata_ts7.json", False),
        ("metadata_ts8.json", True),
        ("metadata_ts9.json", True),
        ("metadata_ts10.json", True),
    ],
)
def test_dataschema_metadata_json(inpath, success, datadir):
    os.chdir(datadir)
    with open(inpath, "r") as infile:
        indict = json.load(infile)
    if not success:
        with pytest.raises(ValidationError):
            to_dataschema(**indict)
    else:
        to_dataschema(**indict)


@pytest.mark.parametrize(
    "inpath",
    [
        ("ts0_dummy.json"),
        ("ts1_dummy.json"),
        ("ts2_dummy.json"),
        ("ts3_basiccsv.json"),
        ("ts4_basiccsv.json"),
        ("ts5_flowdata.json"),
        ("ts6_meascsv.json"),
        ("ts7_electrochem.json"),
    ],
)
def test_dataschema_steps_json(inpath, datadir):
    os.chdir(datadir)
    with open(inpath, "r") as infile:
        jsdata = json.load(infile)
    ref = jsdata["output"]
    ret = to_dataschema(**jsdata["input"])
    assert ret.dict()["steps"] == ref
