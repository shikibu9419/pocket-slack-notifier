# -*- coding: utf-8 -*-
import os
import requests

WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')


def __post_to_slack(payload={}) -> str:
    headers = {
        'Content-Type': 'application/json',
    }

    return requests.post(WEBHOOK_URL, json=payload, headers=headers).text


def notify(tag, pick_up_type, posts) -> str:
    payload = {
        'blocks': [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': f'この記事を読むのです...\nタグ: *{tag}*\nピックアップ方法: *{pick_up_type}*'
                }
            },
            {
                'type': 'divider'
            }
        ]
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
                        'value': post['item_id']
                    }
                ]
            }
        )
        payload['blocks'].append({'type': 'divider'})

    return __post_to_slack(payload)
