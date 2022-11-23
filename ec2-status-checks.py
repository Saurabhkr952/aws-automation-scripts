import boto3
import schedule

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

reservation = ec2_client.describe_instances()


def check_instance_status():
    statuses = ec2_client.describe_instance_status()
    for stats in statuses['InstanceStatuses']:
        instance_id = stats['InstanceId']
        instance_stats = stats['InstanceStatus']['Status']
        system_stats = stats['SystemStatus']['Status']
        instance_state = stats['InstanceState']['Name']

        print(
            f"Instance ID: {instance_id}\nInstance State: {instance_state}\nInstance status: {instance_stats}\nSystem status: {system_stats}\n")

    print("##############################################")


schedule.every(5).seconds.do(check_instance_status)

while True:
    schedule.run_pending()
