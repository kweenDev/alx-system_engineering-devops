#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers for
a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for
    a given subreddit.

    Args:
        subreddit (str): The subreddit name to query.

    Returns:
        int: Number of subscribers for the subreddit.
        Returns 0 if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by/u/RegalRee"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0


if __name__ == '__main__':
    # Example usage
    subreddit_name = input("Enter the subreddit name: ")
    print(
        f"Number of subscribers in r/{subreddit_name}:
        {number_of_subscribers(subreddit_name)}")
