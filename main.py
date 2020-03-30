import json
import os
import random
import requests
from typing import Dict
from slack import notify

POCKET_URL = 'https://getpocket.com/v3/get'
ACCESS_TOKEN = os.environ.get('POCKET_ACCESS_TOKEN')
CONSUMER_KEY = os.environ.get('POCKET_CONSUMER_KEY')

MAX_ARTICLES = os.environ.get('MAX_ARTICLES') or 1
PICK_UP_TYPE = os.environ.get('PICK_UP_TYPE') or 'newest'  # newest / random

TAGS = ['todo', 'business', 'programming']
TAG = os.environ.get('TAG') or random.choice(TAGS)


def get_pocket_list(tag='_untagged_', sort='newest') -> Dict:
    params = {'access_token': ACCESS_TOKEN, 'consumer_key': CONSUMER_KEY, 'tag': TAG, 'count': MAX_ARTICLES}
    return requests.post(POCKET_URL, params=params).json()


if __name__ == '__main__':
    posts = get_pocket_list(tag='todo')['list'].values()
    notify(TAG, PICK_UP_TYPE, posts)
