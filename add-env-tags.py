import boto3

ec2_client_ohio = boto3.client('ec2', region_name='us-east-2')
ec2_resource_ohio = boto3.resource('ec2', region_name='us-east-2')

ec2_client_virginia = boto3.client('ec2', region_name='us-east-1')
ec2_resource_virginia = boto3.resource('ec2', region_name='us-east-1')

instance_ids_ohio = []
instance_ids_virginia = []

reservations_ohio = ec2_client_ohio.describe_instances()['Reservations']
for reservation in reservations_ohio:
    instances = reservation['Instances']
    for instance in instances:
        instance_ids_ohio.append(instance['InstanceId'])


response = ec2_resource_ohio.create_tags(
    Resources=instance_ids_ohio,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        }
    ]
)

reservations_virginia = ec2_client_virginia.describe_instances()['Reservations']
for reservation in reservations_virginia:
    instances = reservation['Instances']
    for instance in instances:
        instance_ids_virginia.append(instance['InstanceId'])


response = ec2_resource_virginia.create_tags(
    Resources=instance_ids_virginia,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        }
    ]
)