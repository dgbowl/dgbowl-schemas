ts0 = {
    "version": "v1.0",
    "load": [
        {
            "as": "sparse",
            "path": "sparse.dg.json",
            "check": True,
            "type": "datagram",
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
            ],
        }
    ],
}

ts1 = {
    "version": "v1.0",
    "load": [
        {
            "as": "sparse",
            "path": "sparse.dg.json",
            "check": True,
            "type": "datagram",
        },
        {
            "as": "norm",
            "path": "normalized.dg.json",
            "check": True,
            "type": "datagram",
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
            ],
        },
        {
            "into": "table 2",
            "from": "norm",
            "at": {"indices": [0, 1, 2]},
        },
        {
            "into": "table 2",
            "from": "norm",
            "at": {"steps": ["a"]},
            "columns": [{"key": "derived->xin->*", "as": "xin"}],
        },
    ],
}

ts2 = {
    "version": "v1.0",
    "load": [
        {
            "as": "norm",
            "path": "normalized.dg.json",
            "check": True,
            "type": "datagram",
        },
        {
            "as": "sparse",
            "path": "sparse.dg.json",
            "check": True,
            "type": "datagram",
        },
    ],
    "extract": [
        {
            "into": "df",
            "from": "norm",
            "at": {"steps": ["a"]},
            "columns": [
                {"key": "raw->T_f", "as": "rawT"},
                {"key": "derived->T", "as": "derT"},
            ],
        },
        {
            "into": "df",
            "from": "sparse",
            "at": {"steps": ["b1", "b2", "b3"]},
            "columns": [{"key": "derived->xout->*", "as": "xout"}],
        },
    ],
}

ts3 = {
    "version": "v1.0",
    "load": [
        {
            "as": "norm",
            "path": "normalized.dg.json",
            "check": True,
            "type": "datagram",
        },
        {
            "as": "sparse",
            "path": "sparse.dg.json",
            "check": True,
            "type": "datagram",
        },
    ],
    "extract": [
        {
            "into": "df",
            "from": "norm",
            "at": {"steps": ["a"]},
            "columns": [
                {"key": "raw->T_f", "as": "rawT"},
                {"key": "derived->T", "as": "derT"},
            ],
        },
        {
            "into": "temp",
            "from": "sparse",
            "at": {"steps": ["b1", "b2", "b3"]},
            "columns": [{"key": "derived->xout->*", "as": "xout"}],
        },
        {
            "into": "df",
            "from": "temp",
            "columns": [{"key": "xout->*", "as": "xout"}],
        },
    ],
}

ts4 = {
    "version": "v1.0",
    "load": [
        {
            "as": "sparse",
            "path": "sparse.dg.json",
            "check": True,
            "type": "datagram",
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
            ],
        },
    ],
    "save": [
        {"table": "table 1", "as": "sparse.pkl", "sigma": True},
        {"table": "table 1", "as": "sparse.json", "sigma": True},
        {"table": "table 1", "as": "sparse.csv", "sigma": True},
        {"table": "table 1", "as": "sparse.xlsx", "sigma": True},
    ],
}

ts5 = {
    "version": "v1.0",
    "load": [
        {
            "as": "sparse",
            "path": "sparse.dg.json",
            "check": True,
            "type": "datagram",
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
            ],
        },
    ],
    "save": [
        {
            "table": "table 1",
            "as": "sparse.extension",
            "type": "csv",
            "sigma": False,
        },
    ],
}

ts6 = {
    "version": "v1.0",
    "load": [
        {
            "as": "dg",
            "path": "normalized.dg.json",
            "check": True,
            "type": "datagram",
        },
    ],
    "extract": [
        {
            "into": "df",
            "from": "dg",
            "at": {"indices": [2, 3, 4]},
            "columns": [
                {"key": "derived->xout->*", "as": "xout"},
            ],
        },
        {
            "into": "df",
            "from": "dg",
            "at": {"indices": [1]},
            "columns": [
                {"key": "derived->xin->*", "as": "xin"},
            ],
        },
    ],
    "transform": [
        {
            "table": "df",
            "with": "catalysis.conversion",
            "using": [
                {
                    "feedstock": "propane",
                    "xin": "xin",
                    "xout": "xout",
                },
                {
                    "feedstock": "propane",
                    "product": False,
                    "xin": "xin",
                    "xout": "xout",
                },
                {
                    "feedstock": "O2",
                    "element": "O",
                    "xin": "xin",
                    "xout": "xout",
                },
            ],
        }
    ],
}

ts7 = {
    "version": "v1.0",
    "load": [
        {
            "as": "dg",
            "path": "normalized.dg.json",
            "check": True,
            "type": "datagram",
        },
    ],
    "extract": [
        {
            "into": "df",
            "from": "dg",
            "at": {"steps": ["b1", "b2", "b3"]},
            "columns": [
                {"key": "derived->xout->*", "as": "xout"},
            ],
        },
        {
            "into": "df",
            "from": "dg",
            "at": {"steps": ["a"]},
            "columns": [
                {"key": "derived->xin->*", "as": "xin"},
            ],
        },
    ],
    "transform": [
        {
            "table": "df",
            "with": "catalysis.selectivity",
            "using": [{"feedstock": "propane", "xin": "xin", "xout": "xout"}],
        },
        {
            "table": "df",
            "with": "catalysis.atom_balance",
            "using": [{"xin": "xin", "xout": "xout"}],
        },
    ],
}

ts8 = {
    "version": "v1.0",
    "load": [
        {
            "as": "dg",
            "path": "normalized.dg.json",
            "check": True,
            "type": "datagram",
        },
    ],
    "extract": [
        {
            "into": "df",
            "from": "dg",
            "at": {"steps": ["b1", "b2", "b3"]},
            "columns": [
                {"key": "derived->xout->*", "as": "xout"},
            ],
        },
        {
            "into": "df",
            "from": "dg",
            "at": {"steps": ["a"]},
            "columns": [
                {"key": "derived->xin->*", "as": "xin"},
            ],
        },
    ],
    "transform": [
        {
            "table": "df",
            "with": "catalysis.selectivity",
            "using": [{"feedstock": "propane", "xin": "xin", "xout": "xout"}],
        },
        {
            "table": "df",
            "with": "catalysis.atom_balance",
            "using": [{"xin": "xin", "xout": "xout"}],
        },
    ],
    "plot": [
        {
            "table": "df",
            "ncols": 1,
            "nrows": 2,
            "ax_args": [
                {
                    "rows": (0, 1),
                    "series": [
                        {
                            "y": "Sp_C->*",
                            "index": {"from_zero": True},
                            "kind": "scatter",
                        }
                    ],
                    "legend": True,
                },
                {
                    "rows": (1, 2),
                    "series": [
                        {
                            "y": "xout->*",
                            "index": {"from_zero": True},
                            "kind": "line",
                        }
                    ],
                    "legend": True,
                },
            ],
            "save": {"as": "test.png"},
        }
    ],
}

ts9 = {
    "version": "v1.0",
    "load": [
        {
            "as": "df",
            "path": "ref.electrochemistry_fe.ts0.pkl",
            "type": "table",
            "check": True,
        },
    ],
    "plot": [
        {
            "table": "df",
            "nrows": 3,
            "ncols": 1,
            "ax_args": [
                {
                    "rows": (0, 2),
                    "series": [
                        {
                            "y": "fe->H2",
                            "index": {"from_zero": True},
                            "kind": "scatter",
                        },
                        {
                            "y": "fe->C2H4",
                            "index": {"from_zero": True},
                            "kind": "scatter",
                        },
                        {
                            "y": "fe->CO",
                            "index": {"from_zero": True},
                            "kind": "scatter",
                        },
                        {
                            "y": "fe->CH4",
                            "index": {"from_zero": True},
                            "kind": "scatter",
                        },
                    ],
                    "legend": True,
                    "ylabel": "$\\eta_F$",
                },
                {
                    "rows": (2, 3),
                    "series": [
                        {
                            "y": "I",
                            "index": {"from_zero": True},
                            "kind": "scatter",
                        },
                    ],
                    "legend": False,
                },
            ],
            "save": {"as": "test.png"},
        }
    ],
}


js0 = {
    "version": "v1.0",
    "load": [
        {"as": "d1", "path": "table.pkl", "type": "table", "check": True},
        {"as": "d2", "path": "dg.json", "type": "datagram", "check": False},
    ],
    "extract": [
        {
            "into": "t1",
            "from": "d2",
            "at": {"indices": [4]},
            "columns": [{"key": "raw->T_f", "as": "rawT"}],
        },
        {
            "into": "t1",
            "constants": [
                {"value": "0.65(5)", "as": "m", "units": "kg"},
                {"value": 0.53, "as": "x"},
            ],
        },
    ],
    "transform": [
        {
            "table": "t1",
            "with": "catalysis.conversion",
            "using": [{"feedstock": "propane", "xin": "xin", "xout": "xout"}],
        }
    ],
    "save": [{"table": "t1", "as": "sparse.csv", "type": "csv", "sigma": False}],
}
