#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Main function """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url,
                            allow_redirects=False,
                            headers={'User-Agent': 'Custom user agent'},
                            params={'after': after})
    if response and response.status_code == 200:
        after = response.json().get('data').get('after')
        post_list = response.json().get('data').get('children')
        for children in post_list:
            hot_list.append(children.get('data').get('title'))
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
