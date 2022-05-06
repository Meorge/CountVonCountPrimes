from pickle import load, dump
from typing import List
from calculate_primality import is_prime

distilled: List[dict] = []
with open('distilled_tweets', 'rb') as f:
    distilled = load(f)

for t in distilled:
    if is_prime(t['number']):
        print(f"{t['date']:%Y-%m-%d %H:%M} - {t['number']}{' (laugh)' if t['hasLaugh'] else ''}")