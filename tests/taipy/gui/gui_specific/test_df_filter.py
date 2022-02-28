from importlib import util

import numpy as np
import pandas as pd

from taipy.gui.data.utils import df_data_filter


def test_data_filter_1(csvdata):
    df, x, y = df_data_filter(csvdata[:1500], None, "Daily hospital occupancy", 100)
    if not util.find_spec("rdp"):
        assert df.shape[0] == 1500
        assert x is None
    else:
        assert df.shape[0] == 121
        assert x == "tAiPy_index_0"
    assert y == "Daily hospital occupancy"


def test_data_filter_2(csvdata):
    df, x, y = df_data_filter(csvdata[:1500], None, "Daily hospital occupancy", 1500)
    assert df.shape[0] == 1500
    assert x is None
    assert y == "Daily hospital occupancy"


def test_data_filter_3(csvdata):
    csvdata["DayInt"] = pd.to_datetime(csvdata["Day"]).view(np.int64)
    df, x, y = df_data_filter(csvdata[:1500], "DayInt", "Daily hospital occupancy", 100)
    if not util.find_spec("rdp"):
        assert df.shape[0] == 1500
    else:
        assert df.shape[0] == 121
    assert x == "DayInt"
    assert y == "Daily hospital occupancy"
