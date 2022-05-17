import pytest
import os
import json
import yaml
from dgbowl_schemas.tomato import to_payload

@pytest.mark.parametrize(
    "inpath",
    [
        "ts0.yml",
        "ts1.yml",
        "ts2.yml",
        "ts3.yml",
        "ts4.yml",
    ],
)
def test_payload_yml(inpath, datadir):
    os.chdir(datadir)
    with open(inpath, "r") as infile:
        indict = yaml.safe_load(infile)
    ret = to_payload(**indict)
    with open(f"ref.{inpath.replace('yml','json')}", "r") as ofile:
        ref = json.load(ofile)
    assert ret == ref