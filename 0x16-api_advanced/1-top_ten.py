#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the top 10 hot
posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the top 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The subreddit name to query.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by/u/RegalRee)"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print("Invalid subreddit. Please try again.")


if __name__ == '__main__':
    # Example usage
    subreddit_name = input("Enter the subreddit name: ")
    top_ten(subreddit_name)
