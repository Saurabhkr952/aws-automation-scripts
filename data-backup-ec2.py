import boto3
import schedule

ec2_client = boto3.client('ec2', region_name='ap-south-1')


def create_volume_snapshots():
    volumes = ec2_client.describe_volumes()
    Filters = [
                  {
                      'Name': 'tag:Name',
                      'Values': [
                          'prod',
                      ]
                  },
              ],
    for ec2_volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=ec2_volume['VolumeId']
        )
    print(new_snapshot)


schedule.every(20).seconds.do(create_volume_snapshots)

while True:
    schedule.run_pending()
