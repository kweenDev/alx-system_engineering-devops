#!/usr/bin/python3
"""
Module to recursively query the Reddit API, parse titles of hot
articles, and print a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively query the Reddit API, parse titles of hot articles,
    and print a sorted count of given keywords.

    Args:
        subreddit (str): The subreddit name to query.
        word_list (list): List of keywords to count occurrences.
        after (str): Parameter for pagination.
        counts (dict): Dictionary to store counts of keywords.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by/u/RegalRee)"}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1

        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit or no hot articles found.")


if __name__ == '__main__':
    # Example usage
    subreddit_name = input("Enter the subreddit name: ")
    keywords = input("Enter keywords separated by spaces: ").split()
    count_words(subreddit_name, keywords)
