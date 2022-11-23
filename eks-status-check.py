import boto3

eks_client = boto3.client('eks', region_name= 'ap-south-1')
cluster_availability = eks_client.list_clusters()
cluster = cluster_availability['clusters']

for cluster in cluster_availability:
    response = eks_client.describe_cluster(
        name=cluster
    )

    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['end-point']
    cluster_version = cluster_info['version']

    print(f" cluster: {cluster} cluster_status: {cluster_status} ")
    print(f"cluster_endpoint: {cluster_endpoint}")
    print(f"cluster_version: {cluster_version}")