import pandas as pd
import boto3
session = boto3.Session(
    aws_access_key_id='AKIA52GMK3P6SDPKCXG5',
    aws_secret_access_key='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'
)

s3 = session.resource('s3')

#%%

from tabulate import tabulate

import awswrangler as wr

obj_s3 = wr.s3.list_objects('s3://lab-spark-edu/01_source')

print(obj_s3)

n=1

for i in obj_s3:

    if n == 1:
       print(i)

    else:
       print(n)

    n = n+1
