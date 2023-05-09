#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:1-top_ten"
    }
    params = {
        "limit": 10
    }
    r = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if r.status_code == 404:
        print("None")
        return
    results = r.json().get("data")
    [print(child.get("data").get("title")) for child in results.get("children")]
