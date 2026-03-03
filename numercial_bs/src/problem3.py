"""
Problem 3: User Event Feature Engineering (Pandas)
====================================================
~10 minutes | Pandas

You work on the ML team at a design platform. You're given a DataFrame of user
design events and need to compute per-user features for a model.

Input DataFrame columns:
    - user_id: str
    - event_type: str (one of "create", "edit", "export", "share")
    - timestamp: datetime
    - design_id: str

Implement:

1. compute_user_features(events: pd.DataFrame) -> pd.DataFrame
   Returns a DataFrame indexed by user_id with these columns:
   - total_events: int - total number of events per user
   - unique_designs: int - number of distinct designs per user
   - most_common_event: str - the event_type that appears most often for each user
                              (if tied, any of the tied values is acceptable)
   - days_active: int - number of distinct calendar dates the user had events on
   - export_rate: float - fraction of the user's events that are "export" events
                          (0.0 if user has no exports)

The returned DataFrame should be sorted by user_id (ascending).
"""

import pandas as pd


def compute_user_features(events: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError
