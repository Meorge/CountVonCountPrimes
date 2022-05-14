from random import random
from traceback import print_exc
from typing import List
from dotenv import load_dotenv
from os import environ
from requests import ReadTimeout
import tweepy
from pickle import load, dump
from parse_number import parse_number
from calculate_primality import is_prime, get_prime_index
import logging
from time import sleep

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='output.log', level=logging.INFO)
logging.info('Starting up the Count von Count bot...')

# Load the environment variables from the .env file
load_dotenv()
consumer_key = environ['API_KEY']
consumer_secret = environ['API_KEY_SECRET']

access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']

bearer_token = environ['BEARER_TOKEN']

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    bearer_token=bearer_token,
    access_token=access_token,
    access_token_secret=access_token_secret)

# When starting the program, load the IDs we have retweeted already
retweeted_ids: List[int] = []
try:
    with open('retweeted_ids', 'rb') as f:
        retweeted_ids = load(f)
except FileNotFoundError:
    pass

logging.info(f'retweeted_ids has {len(retweeted_ids)} items')

def retweet_new_primes():
    logging.info('Looking for new primes to retweet...')

    try:
        response = client.search_recent_tweets(
            "from:CountVonCount",
            max_results=20
        )
    except ReadTimeout:
        logging.error("Looks like there was a timeout")
        print_exc()
        return
        
    tweets = response.data
    
    retweeted_anything = False
    for t in tweets:
        t: tweepy.Tweet
        # Convert the written-out number into an integer
        value = parse_number(t.text)

        # Check if the number is prime
        if not is_prime(value):
            continue

        # Check if we've already retweeted this tweet
        if t.id in retweeted_ids:
            continue

        logging.info(f'Found a non-retweeted prime, {value} - attempting to retweet')
        try:
            laugh = " Ah ah ah!" if random() > 0.5 else ""
            response = client.create_tweet(text=f"That's prime number {get_prime_index(value)}.{laugh}", quote_tweet_id=t.id)
            logging.info(response)
            retweeted_ids.append(t.id)
            retweeted_anything = True
        except TypeError:
            logging.error(f"Failed to retweet {t.id} due to a TypeError")
            print_exc()

    # Save the retweeted IDs to a file, but only if we actually changed the list
    if retweeted_anything:
        with open('retweeted_ids', 'wb') as f:
            dump(retweeted_ids, f)


while True:
    retweet_new_primes()
    # Sleep for two hours
    sleep(7200)