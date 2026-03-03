import pandas as pd
import numpy as np
import pytest
from src.problem3 import compute_user_features


@pytest.fixture
def sample_events():
    return pd.DataFrame({
        "user_id": ["u1", "u1", "u1", "u1", "u2", "u2", "u2", "u3"],
        "event_type": ["create", "edit", "edit", "export", "create", "create", "share", "export"],
        "timestamp": pd.to_datetime([
            "2024-01-01 10:00", "2024-01-01 11:00", "2024-01-02 09:00", "2024-01-02 14:00",
            "2024-01-01 08:00", "2024-01-01 09:00", "2024-01-03 10:00", "2024-01-05 12:00",
        ]),
        "design_id": ["d1", "d1", "d2", "d2", "d3", "d3", "d4", "d5"],
    })


class TestComputeUserFeatures:
    def test_returns_dataframe(self, sample_events):
        result = compute_user_features(sample_events)
        assert isinstance(result, pd.DataFrame)

    def test_index_is_user_id(self, sample_events):
        result = compute_user_features(sample_events)
        assert result.index.name == "user_id"
        assert list(result.index) == ["u1", "u2", "u3"]

    def test_total_events(self, sample_events):
        result = compute_user_features(sample_events)
        assert result.loc["u1", "total_events"] == 4
        assert result.loc["u2", "total_events"] == 3
        assert result.loc["u3", "total_events"] == 1

    def test_unique_designs(self, sample_events):
        result = compute_user_features(sample_events)
        assert result.loc["u1", "unique_designs"] == 2
        assert result.loc["u2", "unique_designs"] == 2
        assert result.loc["u3", "unique_designs"] == 1

    def test_most_common_event(self, sample_events):
        result = compute_user_features(sample_events)
        assert result.loc["u1", "most_common_event"] == "edit"  # edit appears 2x
        assert result.loc["u2", "most_common_event"] == "create"  # create appears 2x
        assert result.loc["u3", "most_common_event"] == "export"

    def test_days_active(self, sample_events):
        result = compute_user_features(sample_events)
        assert result.loc["u1", "days_active"] == 2  # Jan 1 and Jan 2
        assert result.loc["u2", "days_active"] == 2  # Jan 1 and Jan 3
        assert result.loc["u3", "days_active"] == 1  # Jan 5

    def test_export_rate(self, sample_events):
        result = compute_user_features(sample_events)
        assert abs(result.loc["u1", "export_rate"] - 0.25) < 1e-9  # 1/4
        assert abs(result.loc["u2", "export_rate"] - 0.0) < 1e-9   # 0/3
        assert abs(result.loc["u3", "export_rate"] - 1.0) < 1e-9   # 1/1

    def test_column_names(self, sample_events):
        result = compute_user_features(sample_events)
        expected_cols = {"total_events", "unique_designs", "most_common_event",
                         "days_active", "export_rate"}
        assert set(result.columns) == expected_cols

    def test_sorted_by_user_id(self, sample_events):
        # Shuffle input to verify sorting
        shuffled = sample_events.sample(frac=1, random_state=42)
        result = compute_user_features(shuffled)
        assert list(result.index) == sorted(result.index)

    def test_single_user(self):
        events = pd.DataFrame({
            "user_id": ["u1", "u1"],
            "event_type": ["create", "export"],
            "timestamp": pd.to_datetime(["2024-01-01 10:00", "2024-01-01 11:00"]),
            "design_id": ["d1", "d1"],
        })
        result = compute_user_features(events)
        assert result.loc["u1", "total_events"] == 2
        assert result.loc["u1", "unique_designs"] == 1
        assert result.loc["u1", "days_active"] == 1
        assert abs(result.loc["u1", "export_rate"] - 0.5) < 1e-9
