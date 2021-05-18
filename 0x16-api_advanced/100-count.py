#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles
"""
import requests


def count_words(subreddit, word_list, after=None, my_dict={}):
    """ Main function """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url,
                            allow_redirects=False,
                            headers={'User-Agent': 'Custom user agent'},
                            params={'after': after})
    if response and response.status_code == 200:
        post_list = response.json().get('data').get('children')
        for children in post_list:
            title1 = children.get('data').get('title').lower().split()
            for word in word_list:
                try:
                    my_dict[word.lower()] += title1.count(word.lower())
                except KeyError:
                    my_dict[word.lower()] = title1.count(word.lower())
        after = response.json().get('data').get('after')
        if (after is None):
            for key, val in sorted(my_dict.items(),
                                   key=lambda x: (-x[1], x[0])):
                if (val != 0):
                    print("{}: {}".format(key, val))
            return
        return count_words(subreddit, word_list, after, my_dict)
    else:
        return
