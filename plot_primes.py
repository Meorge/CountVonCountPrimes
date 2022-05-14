from pickle import load
from typing import List
from calculate_primality import is_prime
import matplotlib.pyplot as plt

distilled: List[dict]
with open('distilled_tweets', 'rb') as f:
    distilled = load(f)

x = [t['number'] for t in distilled if is_prime(t['number'])]
y = [t['likes'] for t in distilled if is_prime(t['number'])]
plt.scatter(x, y, color='red', marker='.', zorder=2)

x2 = [t['number'] for t in distilled if not is_prime(t['number'])]
y2 = [t['likes'] for t in distilled if not is_prime(t['number'])]
plt.scatter(x2, y2, color='blue', marker='.', zorder=1)

plt.title('@CountVonCount Tweets versus Likes')
plt.xlabel('Number')
plt.ylabel('Likes')
plt.legend(['Prime', 'Non-Prime'])
plt.show()