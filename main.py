import json
import os
import random
import requests
from typing import Dict, List
from slack import notify


POCKET_URL = 'https://getpocket.com/v3/get'
ACCESS_TOKEN = os.environ.get('POCKET_ACCESS_TOKEN')
CONSUMER_KEY = os.environ.get('POCKET_CONSUMER_KEY')

MAX_ARTICLES = os.environ.get('MAX_ARTICLES') or 1
PICK_UP_TYPE = os.environ.get('PICK_UP_TYPE') or 'newest'  # newest / random
AVAILABLE_TAGS = os.environ.get('AVAILABLE_TAGS') or ['todo', 'business', 'programming']
TAG = os.environ.get('TAG') or random.choice(AVAILABLE_TAGS)


def get_pocket_items(tag='_untagged_', sort='newest') -> List[Dict]:
    params = {'access_token': ACCESS_TOKEN, 'consumer_key': CONSUMER_KEY, 'tag': TAG, 'count': MAX_ARTICLES}
    return requests.post(POCKET_URL, params=params).json()['list'].values()


if __name__ == '__main__':
    posts = get_pocket_items(tag='todo')
    notify(TAG, PICK_UP_TYPE, posts)
