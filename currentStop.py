import boto3
from botocore.exceptions import ClientError
instance_id = ['i-00a05f3783a33a207' , 'i-068c2c7606bab82ea' , 'i-0bc350092505d7f55' , 'i-0d46d3dc72930a499']
ec2 = boto3.client('ec2')
# Do a dryrun first to verify permissions
try:
    dresponse = ec2.stop_instances(InstanceIds=['i-00a05f3783a33a207' , 'i-068c2c7606bab82ea' , 'i-0bc350092505d7f55' , 'i-0d46d3dc72930a499'], DryRun=True)
    print (dresponse)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        raise
# Dry run succeeded, run stop_instances without dryrun
try:
    response = ec2.stop_instances(InstanceIds=['i-00a05f3783a33a207' , 'i-068c2c7606bab82ea' , 'i-0bc350092505d7f55' , 'i-0d46d3dc72930a499'], DryRun=False)
    print(response)
    print("The following instances are stopped : ", instance_id)
except ClientError as e:
    print(e)