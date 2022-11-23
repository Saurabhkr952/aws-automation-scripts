import boto3

ec2_client_mumbai = boto3.client('ec2', region_name='ap-south-1')
ec2_resource_paris = boto3.resource('ec2', region_name='ap-south-1')

instance_ids_mumbai = []

mumbai_instances = ec2_client_mumbai.describe_instances()['Reservations']
for res in mumbai_instances:
    mumbai_instances = res['Instances']
    for ins in mumbai_instances:
        instance_ids_mumbai.append(ins['InstanceId'])


response = ec2_resource_paris.create_tags(
    Resources=instance_ids_mumbai,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)


