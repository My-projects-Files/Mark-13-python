import boto3

def lambda_handler(event,context):
    ec2=boto3.client('ec2')
    #Get all the EDS volumes
    response = ec2.describe_snapshots(OwnerIds=['self'])
    #get all active EC2 instance
    instances = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    active_instance_ids = set() #instance ids stored here

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])
    
    #iterate through each snapshot
    for snap in response["Snapshots"]:
        snapshot_id=snap['SnapshotId']
        volume_id=snap.get("VolumeId")
        
        if not volume_id:
            #delete if its not attached to any volumes
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleteing the EBS shapshots {snapshot_id} as it was not attached to volumes")
        else:
            #check if the volume still exists
            try:
                volume_response=ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"deleting the EBS snapshots {snapshot_id} as its associated vol is not attached to ec2")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    #The vol associated with the snapshort is not found
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Delete ebs snapshot {snapshot_id} as its associated volume was not found")    
