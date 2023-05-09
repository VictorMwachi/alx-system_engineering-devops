#!/usr/bin/python3
"""
contains a function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit
"""

import request

def number_of_subscribers(subreddit):
    """returns number of subcribers"""
    if type(subreddit) is str:
        r = request.get("https://www.reddit.com/dev/api/r/{}/about.json".formart(subreddit),
        headers={'User-Agent': '0x16-api_advanced:project:0-subs)'}).json()
        subs = r.get("data", {}).get("subscribers", 0)
        return subs
