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
            "at": {"steps": ["a"], "indices": None, "timestamps": None},
            "columns": [
                {"key": "raw->T_f", "as": "rawT"},
                {"key": "derived->T", "as": "derT"},
            ],
            "constants": None,
        }
    ],
    "transform": None,
    "plot": None,
    "save": None,
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
            "at": {"steps": ["a"], "indices": None, "timestamps": None},
            "columns": [
                {"key": "raw->T_f", "as": "rawT"},
                {"key": "derived->T", "as": "derT"},
            ],
            "constants": None,
        },
        {
            "into": "table 2",
            "from": "norm",
            "at": {"indices": [0, 1, 2], "steps": None, "timestamps": None},
            "columns": None,
            "constants": None,
        },
        {
            "into": "table 2",
            "from": "norm",
            "at": {"steps": ["a"], "indices": None, "timestamps": None},
            "columns": [{"key": "derived->xin->*", "as": "xin"}],
            "constants": None,
        },
    ],
    "transform": None,
    "plot": None,
    "save": None,
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
            "at": {"steps": ["a"], "indices": None, "timestamps": None},
            "columns": [
                {"key": "raw->T_f", "as": "rawT"},
                {"key": "derived->T", "as": "derT"},
            ],
            "constants": None,
        },
        {
            "into": "df",
            "from": "sparse",
            "at": {"steps": ["b1", "b2", "b3"], "indices": None, "timestamps": None},
            "columns": [{"key": "derived->xout->*", "as": "xout"}],
            "constants": None,
        },
    ],
    "transform": None,
    "plot": None,
    "save": None,
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
            "at": {"steps": ["a"], "indices": None, "timestamps": None},
            "columns": [
                {"key": "raw->T_f", "as": "rawT"},
                {"key": "derived->T", "as": "derT"},
            ],
            "constants": None,
        },
        {
            "into": "temp",
            "from": "sparse",
            "at": {"steps": ["b1", "b2", "b3"], "indices": None, "timestamps": None},
            "columns": [{"key": "derived->xout->*", "as": "xout"}],
            "constants": None,
        },
        {
            "into": "df",
            "from": "temp",
            "at": None,
            "columns": [{"key": "xout->*", "as": "xout"}],
            "constants": None,
        },
    ],
    "transform": None,
    "plot": None,
    "save": None,
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
            "at": {"steps": ["a"], "indices": None, "timestamps": None},
            "columns": [
                {"key": "raw->T_f", "as": "rawT"},
                {"key": "derived->T", "as": "derT"},
            ],
            "constants": None,
        },
    ],
    "transform": None,
    "plot": None,
    "save": [
        {"table": "table 1", "as": "sparse.pkl", "sigma": True, "type": None},
        {"table": "table 1", "as": "sparse.json", "sigma": True, "type": None},
        {"table": "table 1", "as": "sparse.csv", "sigma": True, "type": None},
        {"table": "table 1", "as": "sparse.xlsx", "sigma": True, "type": None},
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
            "at": {"steps": ["a"], "indices": None, "timestamps": None},
            "columns": [
                {"key": "raw->T_f", "as": "rawT"},
                {"key": "derived->T", "as": "derT"},
            ],
            "constants": None,
        },
    ],
    "transform": None,
    "plot": None,
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
            "at": {"indices": [2, 3, 4], "steps": None, "timestamps": None},
            "columns": [
                {"key": "derived->xout->*", "as": "xout"},
            ],
            "constants": None,
        },
        {
            "into": "df",
            "from": "dg",
            "at": {"indices": [1], "steps": None, "timestamps": None},
            "columns": [
                {"key": "derived->xin->*", "as": "xin"},
            ],
            "constants": None,
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
    "plot": None,
    "save": None,
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
            "at": {"steps": ["b1", "b2", "b3"], "indices": None, "timestamps": None},
            "columns": [
                {"key": "derived->xout->*", "as": "xout"},
            ],
            "constants": None,
        },
        {
            "into": "df",
            "from": "dg",
            "at": {"steps": ["a"], "indices": None, "timestamps": None},
            "columns": [
                {"key": "derived->xin->*", "as": "xin"},
            ],
            "constants": None,
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
    "plot": None,
    "save": None,
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
            "at": {"steps": ["b1", "b2", "b3"], "indices": None, "timestamps": None},
            "columns": [
                {"key": "derived->xout->*", "as": "xout"},
            ],
            "constants": None,
        },
        {
            "into": "df",
            "from": "dg",
            "at": {"steps": ["a"], "indices": None, "timestamps": None},
            "columns": [
                {"key": "derived->xin->*", "as": "xin"},
            ],
            "constants": None,
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
                    "cols": None,
                    "series": [
                        {
                            "x": None,
                            "y": "Sp_C->*",
                            "index": {"from_zero": True, "to_units": None},
                            "kind": "scatter",
                        }
                    ],
                    "legend": True,
                    "methods": None,
                },
                {
                    "rows": (1, 2),
                    "cols": None,
                    "series": [
                        {
                            "x": None,
                            "y": "xout->*",
                            "index": {"from_zero": True, "to_units": None},
                            "kind": "line",
                        }
                    ],
                    "legend": True,
                    "methods": None,
                },
            ],
            "save": {"as": "test.png", "tight_layout": None},
            "style": None,
            "fig_args": None,
        }
    ],
    "save": None,
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
                    "cols": None,
                    "series": [
                        {
                            "x": None,
                            "y": "fe->H2",
                            "index": {"from_zero": True, "to_units": None},
                            "kind": "scatter",
                        },
                        {
                            "x": None,
                            "y": "fe->C2H4",
                            "index": {"from_zero": True, "to_units": None},
                            "kind": "scatter",
                        },
                        {
                            "x": None,
                            "y": "fe->CO",
                            "index": {"from_zero": True, "to_units": None},
                            "kind": "scatter",
                        },
                        {
                            "x": None,
                            "y": "fe->CH4",
                            "index": {"from_zero": True, "to_units": None},
                            "kind": "scatter",
                        },
                    ],
                    "methods": None,
                    "legend": True,
                    "ylabel": "$\\eta_F$",
                },
                {
                    "rows": (2, 3),
                    "cols": None,
                    "series": [
                        {
                            "x": None,
                            "y": "I",
                            "index": {"from_zero": True, "to_units": None},
                            "kind": "scatter",
                        },
                    ],
                    "legend": False,
                    "methods": None,
                },
            ],
            "fig_args": None,
            "style": None,
            "save": {"as": "test.png", "tight_layout": None},
        }
    ],
    "extract": None,
    "transform": None,
    "save": None,
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
            "at": {"indices": [4], "steps": None, "timestamps": None},
            "constants": None,
            "columns": [{"key": "raw->T_f", "as": "rawT"}],
        },
        {
            "into": "t1",
            "from": None,
            "at": None,
            "constants": [
                {"value": "0.65(5)", "as": "m", "units": "kg"},
                {"value": 0.53, "as": "x", "units": None},
            ],
            "columns": None,
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
    "plot": None,
}

pivot1 = {
    "version": "2.1",
    "load": [
        {
            "as": "tab",
            "path": "table.pkl",
            "type": "table",
            "check": None,
        },
    ],
    "extract": None,
    "pivot": [
        {
            "table": "tab",
            "using": "cycle number",
            "as": "tab_pivot",
            "columns": ["Ewe", "I"],
            "timestamp": "first",
            "timedelta": "t-t0",
        }
    ],
    "transform": None,
    "save": None,
    "plot": None,
}

pivot2 = {
    "version": "2.1",
    "load": [
        {
            "as": "tab",
            "path": "table.pkl",
            "type": "table",
            "check": None,
        },
    ],
    "extract": None,
    "pivot": [
        {
            "table": "tab",
            "using": ["cycle number", "ox/red"],
            "as": "tab_pivot",
            "columns": None,
            "timestamp": "mean",
            "timedelta": None,
        }
    ],
    "transform": None,
    "save": None,
    "plot": None,
}
