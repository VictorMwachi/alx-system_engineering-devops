#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """returns total sucribers else 0"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                     headers={'User-Agent': 'test'})
    subs = r.json().get("data").get("subscribers", 0)
    return subs
