# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import httplib2

from apiclient.discovery import build
from oauth2client.client import OAuth2Credentials

def get_webmasters_service():
    credentials = OAuth2Credentials.from_json(os.environ['OAUTH2_CREDENTIALS_JSON_DATA'])
    http = httplib2.Http()
    http = credentials.authorize(http)
    return build('webmasters', 'v3', http=http)
