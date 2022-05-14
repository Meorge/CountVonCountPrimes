from snscrape.modules.twitter import Tweet
from pickle import load, dump
from typing import List
from parse_number import parse_number

tweets: List[Tweet]
with open('tweets', 'rb') as f:
    tweets = load(f)

tweets.reverse()

distilled: List[dict] = []
for t in tweets:
    if t.sourceLabel != "CountVounCount Counts": continue
    number = parse_number(t.renderedContent)
    hasLaugh = 'Ah ah ah!' in t.renderedContent
    distilled.append({
        'date': t.date,
        'number': number,
        'likes': t.likeCount,
        'replies': t.replyCount,
        'retweets': t.retweetCount,
        'hasLaugh': hasLaugh
    })
    if hasLaugh: print(number)

with open('distilled_tweets', 'wb') as f:
    dump(distilled, f)
    