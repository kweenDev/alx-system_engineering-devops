#!/usr/bin/python3
"""
0-subs.py
Author: Refiloe Radebe
Date: 2024-09-06
Description:
    This script contains a function to query the Reddit API and return
    the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers if valid, 0 otherwise.
    """
    # Define the URL and headers (including a custom User-Agent to avoid blocking)
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditBot/0.1"}

    # Make the request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the status code is 200 (OK)
    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0
