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

from collections import Counter
import pandas as pd


def _row_wise_feature_computation(r: pd.Series) -> tuple[int, str, int, float]:
    total_events = len(r.event_type)
    num_unique_designs = len(r.design_id)
    cl = Counter(r.event_type)
    most_common_event = cl.most_common()[0][0]
    days_active = len(r.date)
    export_rate = 0.0
    if total_events > 0:
        export_rate = cl['export'] / total_events
    return total_events, num_unique_designs, most_common_event, days_active, export_rate


def compute_user_features(events: pd.DataFrame) -> pd.DataFrame:
    events['date'] = events['timestamp'].dt.date
    user_aggs = events[
        ['user_id', 'event_type', 'design_id', 'date']
    ].groupby(['user_id']).agg(
        {
            'design_id': set,
            'date': set,
            'event_type': list,
        }
    )
    user_aggs[[
        "total_events", "unique_designs", "most_common_event", "days_active", "export_rate",
    ]] = user_aggs.apply(
        lambda r: _row_wise_feature_computation(r),
        axis=1,
        result_type='expand',
    )
    return user_aggs[["total_events", "unique_designs", "most_common_event", "days_active", "export_rate"]]

# def compute_user_features(events: pd.DataFrame) -> pd.DataFrame:
#     grouped = events.groupby('user_id')

#     total_events = grouped['event_type'].count()
#     unique_designs = grouped['design_id'].nunique()
    
#     # nope... these two lines are terrible for performance.
#     # rule of thumb: you want to agg with the SIMPLEST vectorised aggregations
#     # e.g. set, count, mean, etc. anything more complex like a lambda basically makes you
#     # loop through a lot.
#     most_common_event = grouped['event_type'].agg(lambda x: x.mode().iloc[0])
#     days_active = grouped['timestamp'].agg(lambda x: x.dt.date.nunique())

#     export_counts = events[events['event_type'] == 'export'].groupby('user_id').size()
#     export_rate = (export_counts / total_events).fillna(0.0)

#     result = pd.DataFrame({
#         'total_events': total_events,
#         'unique_designs': unique_designs,
#         'most_common_event': most_common_event,
#         'days_active': days_active,
#         'export_rate': export_rate,
#     })
#     result.index.name = 'user_id'
#     return result.sort_index()
