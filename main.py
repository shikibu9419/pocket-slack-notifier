import json
import os
import random
import requests
from typing import Dict, List
from slack import notify


POCKET_URL = 'https://getpocket.com/v3/get'
ACCESS_TOKEN = os.environ.get('POCKET_ACCESS_TOKEN')
CONSUMER_KEY = os.environ.get('POCKET_CONSUMER_KEY')

MAX_ARTICLES = os.environ.get('MAX_ARTICLES') or 2
PICK_UP_TYPE = os.environ.get('PICK_UP_TYPE') or 'newest'
TAG = os.environ.get('TAG') or '_untagged_'


def get_pocket_items() -> List[Dict]:
    params = {
        'access_token': ACCESS_TOKEN,
        'consumer_key': CONSUMER_KEY,
        'count': MAX_ARTICLES,
        'sort': PICK_UP_TYPE,
        'tag': TAG
    }
    return requests.post(POCKET_URL, params=params).json()['list'].values()


if __name__ == '__main__':
    posts = get_pocket_items()
    notify(TAG, PICK_UP_TYPE, posts)
