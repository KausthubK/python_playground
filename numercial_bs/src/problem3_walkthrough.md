# Problem 3 Walkthrough: User Event Feature Engineering (Pandas)

## My Solution (Collect + Process)

```python
def compute_user_features(events: pd.DataFrame) -> pd.DataFrame:
    events['date'] = events['timestamp'].dt.date
    user_aggs = events[
        ['user_id', 'event_type', 'design_id', 'date']
    ].groupby(['user_id']).agg({
        'design_id': set,
        'date': set,
        'event_type': list,
    })
    user_aggs[["total_events", "unique_designs", "most_common_event", "days_active", "export_rate"]] = user_aggs.apply(
        lambda r: _row_wise_feature_computation(r), axis=1, result_type='expand',
    )
    return user_aggs[["total_events", "unique_designs", "most_common_event", "days_active", "export_rate"]]
```

### Known issues (not performance):
- **Mutates the input DataFrame** (`events['date'] = ...`) — side effect the caller doesn't expect. Fix: `events = events.copy()` at the top.

## "Pandas-Native" Alternative (Looks Better, Actually Slower)

```python
def compute_user_features(events: pd.DataFrame) -> pd.DataFrame:
    grouped = events.groupby('user_id')

    total_events = grouped['event_type'].count()
    unique_designs = grouped['design_id'].nunique()
    most_common_event = grouped['event_type'].agg(lambda x: x.mode().iloc[0])
    days_active = grouped['timestamp'].agg(lambda x: x.dt.date.nunique())

    export_counts = events[events['event_type'] == 'export'].groupby('user_id').size()
    export_rate = (export_counts / total_events).fillna(0.0)

    result = pd.DataFrame({...})
    result.index.name = 'user_id'
    return result.sort_index()
```

## Benchmark Results (500K rows, 10K users)

```
Original (agg+apply):  2.16s
Native (groupby agg):  3.68s   <-- SLOWER!
```

### Per-operation breakdown of the native approach:
```
count():          0.042s   ✅ fast (C-level)
nunique():        0.121s   ✅ fast (C-level)
mode() lambda:    1.542s   ❌ slow (per-group Python call)
dt.date lambda:   2.102s   ❌ slow (per-group Python call)
export filter:    0.066s   ✅ fast (vectorized)
```

### Why the "native" version is actually slower:
- `mode()` per group and `x.dt.date.nunique()` per group are **still Python-level per-group calls**, just dressed up as pandas
- The original approach does **one groupby pass** into Python containers, then processes with `Counter` (C-implemented in CPython)
- `Counter.most_common()` is faster than `Series.mode()` per group
- `len(set_of_dates)` is faster than `x.dt.date.nunique()` per group

## Key Lesson

**"Pandas-native" is NOT automatically faster.** The real wins come from:

| Aggregation type | Speed | Example |
|---|---|---|
| Built-in string aggs | Fast (C-level) | `count`, `sum`, `mean`, `nunique`, `min`, `max` |
| `.agg(set)` / `.agg(list)` | Medium (one pass, Python containers) | Collect then process |
| Lambda in `.agg()` | Slow (per-group Python + pandas overhead) | `agg(lambda x: x.mode().iloc[0])` |

**Rule of thumb:** If you can't express it as a simple string aggregation (`'count'`, `'nunique'`, `'mean'`, etc.), collecting into Python containers and processing with `Counter`/`set`/`len` in a single `.apply()` pass can actually beat multiple pandas lambdas.

## Interview Q&A

### Q1: Your `.agg(set)` computes `set(design_ids)` per user, then you take `len()`. What pandas method does this in one step?

**`.nunique()`** — counts distinct values per group at the C level. No Python set created.

```python
grouped['design_id'].nunique()
```

### Q2: You're mutating the input DataFrame by adding a `date` column. Is that safe?

**No.** The caller's DataFrame gets an extra column they didn't expect. Could break downstream logic in production ML pipelines where the same DataFrame gets passed through multiple feature functions.

**Fix:** Either `events = events.copy()` at the top, or avoid adding the column altogether by inlining:

```python
grouped['timestamp'].agg(lambda x: x.dt.date.nunique())
```

### Q3: At 100M rows, what's the bottleneck and how would you fix it?

The bottleneck depends on the approach:
- **Native version:** the `mode()` and `dt.date.nunique()` lambdas (3.6s of 3.8s total)
- **Original version:** the `.apply()` pass, but it's actually faster because `Counter` and `set` are C-implemented

**To truly optimize at scale**, replace the expensive aggregations entirely:
- `most_common_event`: do `groupby(['user_id', 'event_type']).size()`, then pick the max per user — fully vectorized
- `days_active`: pre-compute `events['date'] = events['timestamp'].dt.date` (vectorized), then `groupby('user_id')['date'].nunique()` (C-level nunique)
- `export_rate`: filter + groupby + size, then divide — already fast
