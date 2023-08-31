import pytest
import os
import yaml
import json
from dgbowl_schemas.dgpost import to_recipe

from ref_recipe import *


@pytest.mark.parametrize(
    "inpath, outdict",
    [
        ("le_1.yaml", le_1),
        ("le_2.yaml", le_2),
        ("lee_1.yaml", lee_1),
        ("lee_2.yaml", lee_2),
        ("les_1.yaml", les_1),
        ("les_2.yaml", les_2),
        ("les_3.yaml", les_3),
        ("let_1.yaml", let_1),
        ("let_2.yaml", let_2),
        ("letp_1.yaml", letp_1),
        ("lp_1.yaml", lp_1),
        ("pivot_1.yaml", pivot_1),
        ("pivot_2.yaml", pivot_2),
    ],
)
def test_recipe_from_yml(inpath, outdict, datadir):
    os.chdir(datadir)
    with open(inpath, "r") as infile:
        indict = yaml.safe_load(infile)
    ret = to_recipe(**indict).dict(by_alias=True)
    assert outdict == ret


@pytest.mark.parametrize(
    "inpath, outdict",
    [("lets.json", lets)],
)
def test_recipe_from_json(inpath, outdict, datadir):
    os.chdir(datadir)
    with open(inpath, "r") as infile:
        indict = json.load(infile)
    ret = to_recipe(**indict).dict(by_alias=True)
    assert outdict == ret


@pytest.mark.parametrize(
    "inpath",
    [
        ("le_1.yaml"),  # 1.0
        ("letp_1.yaml"),  # 1.0
    ],
)
def test_recipe_update_chain(inpath, datadir):
    os.chdir(datadir)
    with open(inpath, "r") as infile:
        jsdata = yaml.safe_load(infile)
    ret = to_recipe(**jsdata)
    while hasattr(ret, "update"):
        print("here")
        ret = ret.update()
    assert ret.version == "2.1"
