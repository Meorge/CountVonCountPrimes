from pickle import load, dump
from typing import List
from datetime import datetime, timedelta

tweets: List[dict]
with open('distilled_tweets', 'rb') as f:
    tweets = load(f)


# Print out the amount of time between each tweet
for i in range(1, len(tweets) - 1):
    this_date: datetime = tweets[i]['date']
    previous_date: datetime = tweets[i - 1]['date']
    delta: timedelta = this_date - previous_date

    seconds = int(delta.total_seconds())
    hours = seconds // 3600

    print(f"{this_date:%Y-%m-%d %H:%M} ({hours:02d} hrs) - {tweets[i]['number']}")