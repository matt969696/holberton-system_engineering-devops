#!/usr/bin/python3
"""
Gets the number of subscribers from a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ Main function """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url,
                            allow_redirects=False,
                            headers={'User-Agent': 'Custom user agent'})
    if response:
        suscribers_number = response.json().get('data').get('subscribers')
        return suscribers_number
    else:
        return 0
