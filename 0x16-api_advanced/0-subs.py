#!/usr/bin/python3
"""
contains a function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit
"""

def number_of_subscribers(subreddit):
    """returns number of subcribers"""
    url = "https://www.reddit.com/dev/api//r/"
    if subreddit:
        return request.get(f"{url}+{subreditt}")
