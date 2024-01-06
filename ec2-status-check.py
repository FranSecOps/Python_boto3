import boto3
import schedule

ec2_client = boto3.client('ec2', region_name='us-east-1')
ec2_resource = boto3.resource('ec2', region_name='us-east-1')


def check_instances_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances = True
    )
    for status in statuses['InstanceStatuses']:
        inst_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        id = status['InstanceId']
        print(f"Instance: {id} is {state} with instance status: {inst_status} and system status: {sys_status}")

schedule.every(5).minutes.do(check_instances_status)

while True:
    schedule.run_pending()