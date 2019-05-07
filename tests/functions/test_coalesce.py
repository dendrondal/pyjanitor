import numpy as np
import pandas as pd
import pytest


@pytest.mark.functions
def test_coalesce():
    df = pd.DataFrame(
        {"a": [1, np.nan, 3], "b": [2, 3, 1], "c": [2, np.nan, 9]}
    ).coalesce(["a", "b", "c"], "d")
    assert df.shape == (3, 1)
    assert pd.isnull(df).sum().sum() == 0

    df = pd.DataFrame(
        {"a": [1, np.nan, 3], "b": [2, 3, 1], "c": [2, np.nan, 9]}
    ).coalesce(["a", "b", "c"])
    assert df.shape == (3, 1)
    assert pd.isnull(df).sum().sum() == 0

