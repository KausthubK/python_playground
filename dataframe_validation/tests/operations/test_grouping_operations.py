import pandas as pd
import pytest
from pydantic import ValidationError

from dataframe_validation.operations import grouping_operations as sut


def test_success_group_by_group_name(good_input_df, good_output_df):
    out_df = sut.group_by_group_name(good_input_df)
    pd.testing.assert_frame_equal(left=out_df, right=good_output_df, check_exact=True)

def test_fail_group_by_group_name(bad_input_df, good_output_df):
    with pytest.raises(ValidationError):
        out_df = sut.group_by_group_name(bad_input_df)
