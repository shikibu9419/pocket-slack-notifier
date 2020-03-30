# -*- coding: utf-8 -*-

import json
import os
import requests

WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')

def post_to_slack(payload={}):
    headers = {
        'Content-Type': 'application/json',
    }

    print(requests.post(WEBHOOK_URL, json=payload, headers=headers).text)


def notify(tag, pick_up_type, posts):
    payload = {
        'blocks': [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': f'この記事を読むのじゃ...\nタグ: *{tag}*\nピックアップ方法: *{pick_up_type}*'
                }
            },
            {
                'type': 'divider'
            }
        ],
        'unfurl_links': 'true'
    }

    for post in posts:
        payload['blocks'].append(
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': f'"{post["resolved_title"]}"\n{post["resolved_url"]}\n総文字数: {post["word_count"]}'
                },
                'accessory': {
                    'type': 'image',
                    'image_url': post['top_image_url'],
                    'alt_text': post['resolved_title']
                }
            }
        )
        payload['blocks'].append(
            {
                'type': 'actions',
                'elements': [
                    {
                        'type': 'button',
                        'text': {
                            'type': 'plain_text',
                            'text': '読んだ'
                        },
                        'value': 'click_me_123',
                        'url': 'https://google.com'
                    }
                ]
            }
        )
        payload['blocks'].append({'type': 'divider'})

    post_to_slack(payload)
