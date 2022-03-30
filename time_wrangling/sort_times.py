from datetime import datetime as dt

most_recent = dt(2020, 10, 12, 10, 11)
datetime_list = [
    dt(2019, 10, 12, 10, 10),
    dt(2020, 10, 12, 10, 10),
    most_recent
]

print(max(datetime_list))

assert max(datetime_list) == most_recent

print(min(datetime_list))