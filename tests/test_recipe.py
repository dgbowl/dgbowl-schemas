import pytest
import os
import yaml
import json
from dgbowl_schemas.dgpost import to_recipe

from ref_recipe import ts0, ts1, ts2, ts3, ts4, ts5, ts6, ts7, ts8, ts9
from ref_recipe import js0


@pytest.mark.parametrize(
    "inpath, outdict",
    [
        ("le_1.yaml", ts0),
        ("le_2.yaml", ts1),
        ("lee_1.yaml", ts2),
        ("lee_2.yaml", ts3),
        ("les_1.yaml", ts4),
        ("les_2.yaml", ts5),
        ("let_1.yaml", ts6),
        ("let_2.yaml", ts7),
        ("letp_1.yaml", ts8),
        ("lp_1.yaml", ts9),
    ],
)
def test_recipe_from_yml(inpath, outdict, datadir):
    os.chdir(datadir)
    with open(inpath, "r") as infile:
        indict = yaml.safe_load(infile)
    ret = to_recipe(**indict).dict(by_alias=True, exclude_none=True)
    assert outdict == ret


@pytest.mark.parametrize(
    "inpath, outdict",
    [("lets.json", js0)],
)
def test_recipe_from_json(inpath, outdict, datadir):
    os.chdir(datadir)
    with open(inpath, "r") as infile:
        indict = json.load(infile)
    ret = to_recipe(**indict).dict(by_alias=True, exclude_none=True)
    assert outdict == ret
