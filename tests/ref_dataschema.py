ts0 = {
    "metadata": {
        "provenance": "manual",
        "version": "0.1",
        "timezone": "localtime",
        "provenance_metadata": None,
    },
    "steps": [
        {
            "parser": "dummy",
            "input": {
                "files": ["dummy_schema_1.json"],
                "prefix": None,
                "suffix": None,
                "contains": None,
                "exclude": None,
                "encoding": "UTF-8",
            },
            "tag": None,
            "parameters": None,
            "export": None,
            "externaldate": None,
        }
    ],
}

ts1 = {
    "metadata": {
        "provenance": "manual",
        "version": "0.1",
        "timezone": "localtime",
        "provenance_metadata": None,
    },
    "steps": [
        {
            "parser": "dummy",
            "input": {
                "files": ["dummy_schema_1.json"],
                "prefix": None,
                "suffix": None,
                "contains": None,
                "exclude": None,
                "encoding": "UTF-8",
            },
            "tag": None,
            "parameters": None,
            "export": None,
            "externaldate": None,
        },
        {
            "parser": "dummy",
            "input": {
                "files": [
                    ".\\ts0_dummy.json",
                    ".\\ts1_dummy.json",
                    ".\\ts2_basiccsv.json",
                    ".\\ts3_basiccsv.json",
                    ".\\ts4_drycal.json",
                ],
                "prefix": None,
                "suffix": ".json",
                "contains": "dummy",
                "exclude": None,
                "encoding": "UTF-8",
            },
            "tag": None,
            "parameters": {"k": "v", "parser": "dummy"},
            "export": None,
            "externaldate": None,
        },
    ],
}

ts2 = {
    "metadata": {
        "provenance": "manual",
        "version": "0.1",
        "timezone": "localtime",
        "provenance_metadata": None,
    },
    "steps": [
        {
            "parser": "basiccsv",
            "input": {
                "files": ["measurement.csv"],
                "prefix": None,
                "suffix": None,
                "contains": None,
                "exclude": None,
                "encoding": "UTF-8",
            },
            "tag": None,
            "parameters": {
                "convert": None,
                "parser": "basiccsv",
                "sep": ";",
                "sigma": {
                    "T_f": {"atol": 0.05, "rtol": None},
                    "N2": {"atol": 0.005, "rtol": None},
                    "O2": {"atol": 0.005, "rtol": None},
                    "alkane": {"atol": 0.005, "rtol": None},
                    "flow low": {"atol": 0.0005, "rtol": None},
                    "flow high": {"atol": 0.005, "rtol": None},
                },
                "calfile": "fhi_tfcal.json",
                "timestamp": {"timestamp": {"index": 0, "format": "%Y-%m-%d-%H-%M-%S"}},
                "units": None,
            },
            "export": None,
            "externaldate": None,
        }
    ],
}

ts3 = {
    "metadata": {
        "provenance": "manual",
        "version": "0.1",
        "timezone": "localtime",
        "provenance_metadata": None,
    },
    "steps": [
        {
            "parser": "basiccsv",
            "input": {
                "files": ["measurement.csv"],
                "prefix": None,
                "suffix": None,
                "contains": None,
                "exclude": None,
                "encoding": "UTF-8",
            },
            "tag": None,
            "parameters": {
                "convert": None,
                "parser": "basiccsv",
                "sep": ",",
                "sigma": None,
                "calfile": None,
                "timestamp": {
                    "date": {"index": 0, "format": None},
                    "time": {"index": 1, "format": None},
                },
                "units": None,
            },
            "export": None,
            "externaldate": None,
        }
    ],
}

ts4 = {
    "metadata": {
        "provenance": "manual",
        "version": "0.1",
        "timezone": "UTC",
        "provenance_metadata": None,
    },
    "steps": [
        {
            "parser": "flowdata",
            "input": {
                "files": ["Cp_100mA_1mindelay.rtf"],
                "prefix": None,
                "suffix": None,
                "contains": None,
                "exclude": None,
                "encoding": "UTF-8",
            },
            "tag": None,
            "parameters": {
                "convert": None,
                "parser": "flowdata",
                "filetype": "drycal.rtf",
                "calfile": None,
            },
            "export": None,
            "externaldate": {"mode": "add", "using": {"isostring": "2021-09-17"}},
        }
    ],
}
