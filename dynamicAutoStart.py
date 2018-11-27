from __future__ import print_function  # Python 2/3 compatibility
import boto3
import datetime
import sys


def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    client = boto3.client('ec2')
    #instances = ec2.instances.all()
    instances = ec2.instances.filter(Filters=[{'Name':'tag:TeamOwner', 'Values':['TelecomLab']},{'Name':'tag:AutoStart', 'Values':['true']},{'Name': 'instance-state-name', 'Values': ['stopped','stopping']}])
    print("Instance details printing")
    for instance in instances:
        print("instance is : ",instance)
        print(instance.id, instance.instance_type)
		
    print("Instance tag details printing")
    for instance in instances:
        print("instance is : ",instance)
        print("instance id & type : " ,instance.id, instance.instance_type)
        for tag in instance.tags:
            print("tag & value : " ,tag['Key'], tag['Value'])

    scheduled_instances = [instance.id for instance in instances]
    print("scheduled_instances : " ,scheduled_instances)
    if len(scheduled_instances) > 0:
        response = client.start_instances(InstanceIds=scheduled_instances)
        print("response : " ,response)
    else:
        print("No instances to start")   