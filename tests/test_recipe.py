import pytest
import os
import yaml
from dgbowl_schemas.dgpost_recipe import recipe_parser

@pytest.mark.parametrize(
    "inpath, outdict",
    [
        (
            "le_1.yaml",
            {
                "version": "v1.0",
                "load": [
                    {
                        "as": "sparse", 
                        "path": "sparse.dg.json",
                        "check": True,
                        "type": "datagram"
                    }
                ],
                "extract": [
                    {
                        "into": "table 1",
                        "from": "sparse",
                        "at": {"steps": ["a"]},
                        "columns": [
                            {"key": "raw->T_f", "as": "rawT"},
                            {"key": "derived->T", "as": "derT"},
                        ]
                    }
                ]
            }
        ),
        (
            "le_2.yaml",
            {
                "version": "v1.0",
                "load": [
                    {
                        "as": "sparse", 
                        "path": "sparse.dg.json",
                        "check": True,
                        "type": "datagram"
                    },
                    {
                        "as": "norm", 
                        "path": "normalized.dg.json",
                        "check": True,
                        "type": "datagram"
                    },

                ],
                "extract": [
                    {
                        "into": "table 1",
                        "from": "sparse",
                        "at": {"steps": ["a"]},
                        "columns": [
                            {"key": "raw->T_f", "as": "rawT"},
                            {"key": "derived->T", "as": "derT"},
                        ]
                    },
                    {
                        "into": "table 2",
                        "from": "norm",
                        "at": {"steps": ["b1", "b2", "b3"]},
                    },
                    {
                        "into": "table 2",
                        "from": "norm",
                        "at": {"steps": ["a"]},
                        "columns": [
                            {"key": "derived->xin->*", "as": "xin"}
                        ],
                    },
                ]
            }
        )
    ]
)
def test_recipe_from_yml(inpath, outdict, datadir):
    os.chdir(datadir)
    with open(inpath, "r") as infile:
        indict = yaml.safe_load(infile)
    ret = recipe_parser(indict)
    assert outdict == ret