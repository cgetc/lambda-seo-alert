# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import json
import boto3

def invoke(function_name, data):
    client = boto3.client('lambda', region_name=os.environ['AWS_REGION'])

    response = client.invoke(
        FunctionName=function_name,
        InvocationType='Event',
        LogType='Tail',
        Payload=json.dumps(data)
    )
    return True