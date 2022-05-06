from snscrape.modules.twitter import Tweet
from pickle import load
from typing import List
from parse_number import parse_number

tweets: List[Tweet]
with open('tweets', 'rb') as f:
    tweets = load(f)

for t in tweets:
    if t.sourceLabel != "CountVounCount Counts": continue
    # print(f'{t.date:%Y-%m-%d %H:%M} ({t.sourceLabel}) - {t.renderedContent}')
    parse_number(t.renderedContent)