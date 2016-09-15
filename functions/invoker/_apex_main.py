# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import re
import json

from app import task

with open('.env.json') as f:
    os.environ.update(json.load(f, encoding='utf-8'))

def handle(event, context):
    result = {}
    url_list = re.split('/[,\s]+/', os.environ['URL_LIST'])
    for url in url_list:
        if task.invoke('seo_alert_task', {'url': url}):
            result[url] = True
    return result