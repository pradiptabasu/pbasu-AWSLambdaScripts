import boto3
from botocore.exceptions import ClientError
instance_id = ['i-00a05f3783a33a207', 'i-0bf866a22fab3eca2' , 'i-0bc350092505d7f55' , 'i-0d46d3dc72930a499' , 'i-0c07b7cd7f3913225']
scheduled_instances = []
valu = "TeamOwner"
ec2 = boto3.client('ec2')
#client = boto3.resources('ec2')
#adding the filter for instances in EC2
instances = ec2.describe_instances(Filters=[{'Name': 'tag:TeamOwner', 'Values':["TelecomLab"]}])
for instance in instances:
    for tag in instances.tags:
        #if tag['Key'] == valu:
        scheduled_instances.append({'instance':instance, 'schedule':tag['Value']})
        print ("Schedule instances are : ",scheduled_instances);
# Do a dryrun first to verify permissions
try:
    print ('Hello World')
    #dresponse = ec2.start_instances(InstanceIds=['i-00a05f3783a33a207' , 'i-068c2c7606bab82ea' , 'i-0bc350092505d7f55' , 'i-0d46d3dc72930a499'], DryRun=True)
    #print (dresponse)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        raise
# Dry run succeeded, run start_instances without dryrun
try:
    #response = ec2.start_instances(InstanceIds=['i-00a05f3783a33a207' , 'i-068c2c7606bab82ea' , 'i-0bc350092505d7f55' , 'i-0d46d3dc72930a499'], DryRun=False)
    #print(response)
    print("The following instances are started : ", instance_id)
except ClientError as e:
    print(e)
