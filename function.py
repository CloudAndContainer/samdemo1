from __future__ import print_function

import json
import boto3

ec2 = boto3.client('ec2')

print('Loading function \n')


def lambda_handler(event, context):
    # create filter for stopped instances
    instance_filters = [{
                'Name': 'instance-state-name',
                'Values': ['stopped']
    }]

    # get instances that are stopped
    instance_status_response = ec2.describe_instance_status(Filters=instance_filters,IncludeAllInstances=True)

    # iterate through the response to print just the instance id of stopped instances
    for instance in instance_status_response['InstanceStatuses']:
        print (instance['InstanceId'])

    return 'End Function'
