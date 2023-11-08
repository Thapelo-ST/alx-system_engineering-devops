#!/usr/bin/python3
""" returns a top 10 hot posts for a specific subreddit """
import requests


def top_ten(subreddit):
    """
    returns latest top 10 hot post
    example of ussage(outputs may differ):
    """
    headers = {'User-Agent': 'MyRedditBot/1.0 (by /u/your_username)'}

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                for post in posts:
                    title = post['data']['title']
                    print(title)
            else:
                print("None")
        else:
            print("None")
    except requests.RequestException:
        print("None")
