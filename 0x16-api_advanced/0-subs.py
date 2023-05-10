#!/usr/bin/python3
"""
contains a function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """returns number of subcribers"""
    if subreddit is not None and type(subreddit) is str:
        ur = "https://www.reddit.com/dev/api/r/{}/about.json".format(subreddit)
        headers = {'User-Agent': 'test'}
        r = requests.get(url, headers=headers).json()
        subs = r.get("data", {}).get("subscribers", 0)
        return subs
    else:
        return 0
