#!/usr/bin/python3
"""
Prints hot posts on a given Reddit subreddit
"""
import requests


def top_ten(subreddit):
    """ Main function """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    response = requests.get(url,
                            allow_redirects=False,
                            headers={'User-Agent': 'Custom user agent'},
                            params={'limit': 10})
    if response:
        top_list = response.json().get('data').get('children')
        for children in top_list:
            print(children.get('data').get('title'))
    else:
        print(None)
