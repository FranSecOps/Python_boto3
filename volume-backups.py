import boto3

ec2_client = boto3.client('ec2', region_name='us-east-1')

def create_volume_snapshots():
    volumes = ec2_client.describe_volumes()
    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        ec2_client.create_snapshot(
            VolumeId=volume_id
        )

create_volume_snapshots()

snap_ids = []

snapshots = ec2_client.describe_snapshots(
    OwnerIds=['173510818124']
)
for snapshot in snapshots['Snapshots']:
    snap_ids.append(snapshot['SnapshotId'])

for snap in snap_ids:
    print(f'snapshot id: {snap}')