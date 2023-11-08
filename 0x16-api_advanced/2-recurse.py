#!/usr/bin/python3
"""
returns a top 10 hot posts for a specific subreddit using recursion
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    returns a top 10 hot posts for a specific
    subreddit using recursion
    """

    if hot_list is None:
        hot_list = []

    headers = {'User-Agent': 'MyRedditBot/1.0 (by /u/your_username)'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10&after={}".format(
        subreddit, after)

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
