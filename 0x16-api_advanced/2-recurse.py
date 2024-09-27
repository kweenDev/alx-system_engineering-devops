#!/usr/bin/python3
"""
Module to recursively query the Reddit API and return a list containing
titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API and return a list containing
    titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The subreddit name to query.
        hot_list (list): List to store titles of hot articles.
        after (str): Parameter for pagination.

    Returns:
        list: List containing titles of all hot articles. Returns
        None if no results found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by/u/RegalRee)"}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None


if __name__ == '__main__':
    # Example usage
    subreddit_name = input("Enter the subreddit name: ")
    result = recurse(subreddit_name)
    if result:
        print(f"Total hot articles in r/{subreddit_name}: {len(result)}")
    else:
        print("Invalid subreddit or no hot articles found.")
