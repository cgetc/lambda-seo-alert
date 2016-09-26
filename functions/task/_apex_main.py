# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import json
import requests

from app import services

with open('.env.json') as f:
    os.environ.update(json.load(f, encoding='utf-8'))

def handle(event, context):
    site_url = event['url']
    webmasters_service = services.get_webmasters_service()
    result = webmasters_service.urlcrawlerrorscounts().query(siteUrl=site_url).execute()
    attachments = []
    for data in result['countPerTypes']:
        count = sum(int(x['count']) for x in data['entries'])
        if count > 0:
            attachments.append(gen_attachment(data, count))

    if attachments:
        url = os.environ['WEBHOOK_URL']
        payload = {
            'text': 'Crawl Error',
            'attachments': attachments
        }
        r = requests.post(url, json=payload)
        print(r.text)
        return 'post'

    return 'pass'

def gen_attachment(data, count):
    return {
        'color': '#A6374F',
        'author_name': data['platform'],
        'title': '{} {}'.format(count, data['category'])
    }
    
