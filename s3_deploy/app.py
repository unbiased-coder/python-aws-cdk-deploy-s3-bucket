#!/usr/bin/env python3
import os
from dotenv import load_dotenv

# load our env file
print ('Loading env file')
load_dotenv()

import aws_cdk as cdk

from s3_deploy.s3_deploy_stack import S3DeployStack

print ('Creating environment')
cdk_env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))


app = cdk.App()
S3DeployStack(
    app, 
    "S3DeployStack",
    env=cdk_env
)

# synthesize it
print ('Synthesizing stack')
app.synth()
