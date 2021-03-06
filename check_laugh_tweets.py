from pickle import load, dump
from typing import List
import matplotlib.pyplot as plt

plot_against_self = True

distilled: List[dict]
with open('distilled_tweets', 'rb') as f:
    distilled = [t for t in load(f) if t['hasLaugh']]

plt.plot(
    [t['number' if plot_against_self else 'date'] for t in distilled],
    [t['number'] for t in distilled],
    'r.',
    markersize=2)
plt.title('Count von Count Tweets with \'Ah ah ah!\' versus Timestamp')
plt.xlabel(f'{"Number where" if plot_against_self else "Time when"} he went \'Ah ah ah!\'')
plt.ylabel('Number where he went \'Ah ah ah!\'')
plt.show()