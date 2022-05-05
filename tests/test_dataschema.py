import pytest
import os
import yaml
import json
from dgbowl_schemas.yadg_dataschema import DataSchema

from ref_dataschema import ts0, ts1, ts2, ts3, ts4, ts5


@pytest.mark.parametrize(
    "inpath, ref",
    [
        ("ts0_dummy.json", ts0),
        ("ts1_dummy.json", ts1),
        ("ts2_basiccsv.json", ts2),
        ("ts3_basiccsv.json", ts3),
        ("ts4_drycal.json", ts4),
        ("ts5_drycal.json", ts5),
    ],
)
def test_dataschema_from_json(inpath, ref, datadir):
    os.chdir(datadir)
    with open(inpath, "r") as infile:
        indict = json.load(infile)
    ret = DataSchema(**indict)
    assert ret.dict() == ref
