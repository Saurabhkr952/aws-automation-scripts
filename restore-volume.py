import boto3

ec2_client = boto3.client('ec2', region_name='ap-south-1')
resource = boto3.resource('ec2', region_name='ap-south-1')

instance_id = 'i-0231dbd9c11b9876e'

volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)

instance_volume = volumes['Volumes'][0]


response = ec2_client.describe_snapshots()




