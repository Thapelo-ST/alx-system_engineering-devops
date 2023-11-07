#!/usr/bin/python3
""" returns a number of subcribers for a specific subreddit """
import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'MyRedditBot/1.0 (by /u/your_username)'}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers)
