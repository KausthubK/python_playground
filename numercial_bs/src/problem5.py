"""
Problem 5: Rolling Anomaly Detection (Pandas + NumPy)
======================================================
~12 minutes | Pandas + NumPy

You're monitoring a time series of ML model prediction latencies. You need to
flag anomalous spikes using a rolling z-score approach.

Implement:

1. detect_anomalies(
       df: pd.DataFrame,
       value_col: str,
       window: int,
       threshold: float
   ) -> pd.DataFrame

   Parameters:
   - df: DataFrame with at least a column named `value_col` containing numeric values.
         Assume rows are already sorted by time.
   - value_col: name of the column to analyze
   - window: size of the rolling window for computing mean and std
   - threshold: number of standard deviations to flag as anomalous

   Returns a NEW DataFrame (don't modify the input) with the original columns PLUS:
   - "rolling_mean": the rolling mean with the given window size (use min_periods=1
     so early rows still get a value)
   - "rolling_std": the rolling std with the given window size (use min_periods=1)
   - "z_score": abs(value - rolling_mean) / rolling_std
                If rolling_std is 0 (or NaN), z_score should be 0.0
   - "is_anomaly": boolean, True if z_score > threshold

Notes:
   - Use pandas .rolling() with min_periods=1
   - For rolling_std, pandas uses ddof=1 by default. That's fine, keep it.
   - When there's only 1 data point in the window, std will be NaN - treat that as 0.
"""

import pandas as pd
import numpy as np


def detect_anomalies(
    df: pd.DataFrame,
    value_col: str,
    window: int,
    threshold: float,
) -> pd.DataFrame:
    df_copy = df.copy(deep=True)
    df_copy['rolling_mean'] = df_copy[value_col].rolling(window=window, min_periods=1).mean()
    df_copy['rolling_std'] = df_copy[value_col].rolling(window=window, min_periods=1).std()
    df_copy['z_score'] = abs(df_copy[value_col] - df_copy['rolling_mean']) / df_copy['rolling_std']
    df_copy['z_score'] = df_copy['z_score'].fillna(0.0)
    df_copy['is_anomaly'] = df_copy["z_score"] > threshold
    return df_copy
