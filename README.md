# Reddit API Project
## 0x16. API advanced

## Description
This project consists of Python scripts that interact with the Reddit API to perform various tasks such as querying the number of subscribers for a subreddit, retrieving the titles of hot posts, counting occurrences of keywords in hot articles, and more.

## Getting Started
To run these scripts, make sure you have Python 3 installed along with the requests library. You can install the library using the following command:
```bash
pip3 install requests
```

## Usage
1. **Number of Subscribers**
    - Script: `0-subs.py`
    - Usage: `python3 0-main.py [subreddit]`

2. **Top Ten Hot Posts**
    - Script: `1-top_ten.py`
    - Usage: `python3 1-main.py [subreddit]`

3. **Recurse Hot Articles**
    - Script: `2-recurse.py`
    - Usage: `python3 2-main.py [subreddit]`

4. **Count Keywords**
    - Script: `100-count.py`
    - Usage: `python3 100-main.py [subreddit] [keyword_list]`

## Files
- `0-subs.py`: Script to query the number of subscribers for a subreddit.
- `1-top_ten.py`: Script to retrieve the titles of the top ten hot posts for a subreddit.
- `2-recurse.py`: Script to recursively fetch all hot articles for a subreddit.
- `100-count.py`: Script to count occurrences of keywords in hot articles for a subreddit.

## Author
[Refiloe Radebe](https://github.com/kweenDev)
