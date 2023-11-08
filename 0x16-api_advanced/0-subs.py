#!/usr/bin/python3
""" returns a number of subcribers for a specific subreddit """
import requests


def number_of_subscribers(subreddit):
    """
    returns number of subscribers for a given sub reddit
    example of ussage:  python3 0-main.py programming
            output:    756024
    """
    headers = {'User-Agent': 'MyRedditBot/1.0 (by /u/your_username)'}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except requests.RequestException:
        return 0
