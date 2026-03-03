import pandas as pd
import numpy as np
import pytest
from src.problem5 import detect_anomalies


@pytest.fixture
def latency_data():
    return pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=10, freq="h"),
        "latency_ms": [100, 102, 98, 101, 99, 500, 103, 97, 101, 100],
    })


class TestDetectAnomalies:
    def test_returns_new_dataframe(self, latency_data):
        result = detect_anomalies(latency_data, "latency_ms", window=3, threshold=2.0)
        assert result is not latency_data
        # Original should be unchanged
        assert "is_anomaly" not in latency_data.columns

    def test_output_columns(self, latency_data):
        result = detect_anomalies(latency_data, "latency_ms", window=3, threshold=2.0)
        expected_new_cols = {"rolling_mean", "rolling_std", "z_score", "is_anomaly"}
        assert expected_new_cols.issubset(set(result.columns))
        # Original columns preserved
        assert "timestamp" in result.columns
        assert "latency_ms" in result.columns

    def test_same_row_count(self, latency_data):
        result = detect_anomalies(latency_data, "latency_ms", window=3, threshold=2.0)
        assert len(result) == len(latency_data)

    def test_spike_detected(self):
        # Large stable window so spike doesn't dominate the rolling stats
        stable = [100] * 20
        df = pd.DataFrame({"latency_ms": stable + [500] + stable})
        result = detect_anomalies(df, "latency_ms", window=10, threshold=2.0)
        # The spike at index 20 should be flagged
        assert result.loc[20, "is_anomaly"] == True

    def test_normal_values_not_flagged(self, latency_data):
        result = detect_anomalies(latency_data, "latency_ms", window=3, threshold=2.0)
        # Normal values around 100 should not be flagged (check a few)
        assert result.loc[0, "is_anomaly"] == False
        assert result.loc[1, "is_anomaly"] == False
        assert result.loc[9, "is_anomaly"] == False

    def test_rolling_mean_uses_min_periods(self):
        """First row should still have a rolling_mean (min_periods=1)."""
        df = pd.DataFrame({"val": [10, 20, 30]})
        result = detect_anomalies(df, "val", window=5, threshold=2.0)
        # First row: rolling mean of just [10] = 10
        assert abs(result.loc[0, "rolling_mean"] - 10.0) < 1e-9

    def test_zero_std_handling(self):
        """When all values in window are identical, std=0, z_score should be 0."""
        df = pd.DataFrame({"val": [5, 5, 5, 5, 5]})
        result = detect_anomalies(df, "val", window=3, threshold=1.0)
        assert all(result["z_score"] == 0.0)
        assert all(result["is_anomaly"] == False)

    def test_single_row(self):
        """Single row: std is NaN -> z_score should be 0, not anomaly."""
        df = pd.DataFrame({"val": [42]})
        result = detect_anomalies(df, "val", window=3, threshold=2.0)
        assert result.loc[0, "z_score"] == 0.0
        assert result.loc[0, "is_anomaly"] == False

    def test_custom_threshold(self):
        """With a very low threshold, more points get flagged."""
        df = pd.DataFrame({"val": [10, 12, 10, 11, 10]})
        result_strict = detect_anomalies(df, "val", window=3, threshold=0.1)
        result_loose = detect_anomalies(df, "val", window=3, threshold=10.0)
        assert result_strict["is_anomaly"].sum() >= result_loose["is_anomaly"].sum()

    def test_is_anomaly_is_boolean(self, latency_data):
        result = detect_anomalies(latency_data, "latency_ms", window=3, threshold=2.0)
        assert result["is_anomaly"].dtype == bool
