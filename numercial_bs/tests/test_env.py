def test_pandas():
    try:
        import pandas
    except:
        assert False, "Unable to import pandas. Check pip environment is installed correctly"


def test_pytest():
    try:
        import pytest
    except:
        assert False, "Unable to import pytest. Check pip environment is installed correctly"


def test_numpy():
    try:
        import numpy
    except:
        assert False, "Unable to import numpy. Check pip environment is installed correctly"
