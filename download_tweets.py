from snscrape.modules.twitter import TwitterSearchScraper, Tweet
from typing import List
from pickle import dump

tweets: List[Tweet] = []
s = TwitterSearchScraper("from:CountVonCount")

for t in s.get_items():
    t: Tweet
    print(f'{t.date:%y-%m-%d %H:%M} - {t.renderedContent} - ')
    tweets.append(t)

print(f'{len(tweets)} tweets found')

with open('tweets', 'wb') as f:
    dump(tweets, f)

print('Done')