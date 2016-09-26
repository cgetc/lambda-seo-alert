# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import re
import json
import urllib

from app import task

with open('.env.json') as f:
    os.environ.update(json.load(f, encoding='utf-8'))

def handle(event, context):
    result = {}
    res = urllib.urlopen(os.environ['URL_LIST_JSON_URL'])
    url_list = json.loads(res.read())
    for url in url_list:
        if task.invoke('seo_alert_task', {'url': url}):
            result[url] = True
    return result