# python-automation-scripts

In this repository, you will find a collection of powerful automation scripts developed using Boto3, the AWS SDK for Python. These scripts are designed to automate various tasks and manage AWS resources efficiently.

What is Boto3?
Boto3 is a Python library for interacting with AWS services. It allows developers to write Python code to automate and manage various AWS resources and services.

## Prerequisites:
Before using these automation scripts, ensure you have the following prerequisites in place:

1. Install AWS CLI: Install the AWS Command Line Interface (CLI) by following the instructions provided in the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) The AWS CLI is a prerequisite for configuring your AWS credentials.
  
2. Configure AWS Credentials: Configure your AWS credentials using the ```aws configure``` command. This configuration allows the scripts to authenticate and access your AWS resources.

3. Install Boto3 Library: Install the Boto3 library by running ```pip install boto3``` in your command line. This library enables Python scripts to interact with AWS services seamlessly.
 
5. Run the Python Scripts: To execute a specific automation script, run ```python <script_name>.py``` in your command line, replacing <script_name> with the actual name of the Python script file. Make sure you are in the correct directory where the script is located.


## Available Scripts:
Here's a list of the automation scripts included in this repository:

cleanup-snapshot.py: Automate the cleanup of old snapshots.
data-backup-ec2.py: Automate the creation of snapshots for EC2 volumes.
ec2-add-tags.py: Add environment tags to EC2 instances for better organization.
ec2-status-checks.py: Perform health checks and retrieve status information for EC2 instances.
eks-status-check.py: Obtain information about your EKS cluster.
restore-volume.py: Automate the restoration of an EC2 volume from backup.

