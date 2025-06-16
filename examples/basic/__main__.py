"""
Basic example of Aurora Serverless deployment
This example shows the minimal configuration needed to deploy Aurora Serverless
"""

import pulumi
import pulumi_aws as aws
from pulumi_aws import rds, ec2

# Simple configuration
config = pulumi.Config()
master_password = config.require_secret("master_password")

# Get default VPC
default_vpc = ec2.get_vpc(default=True)
default_subnets = ec2.get_subnets(filters=[
    {"name": "vpc-id", "values": [default_vpc.id]}
])

# Create DB Subnet Group
db_subnet_group = rds.SubnetGroup("example-subnet-group",
    subnet_ids=default_subnets.ids,
    tags={"Name": "aurora-example-subnet-group"}
)

# Create Security Group
security_group = ec2.SecurityGroup("example-aurora-sg",
    name="aurora-example-sg",
    description="Security group for Aurora example",
    vpc_id=default_vpc.id,
    ingress=[
        ec2.SecurityGroupIngressArgs(
            from_port=3306,
            to_port=3306,
            protocol="tcp",
            cidr_blocks=["0.0.0.0/0"],  # Restrict this in production
        ),
    ],
    egress=[
        ec2.SecurityGroupEgressArgs(
            from_port=0,
            to_port=0,
            protocol="-1",
            cidr_blocks=["0.0.0.0/0"],
        ),
    ],
    tags={"Name": "aurora-example-security-group"}
)

# Create Aurora Serverless Cluster
aurora_cluster = rds.Cluster("example-aurora-cluster",
    cluster_identifier="aurora-example",
    engine="aurora-mysql",
    engine_version="8.0.mysql_aurora.3.02.0",
    engine_mode="provisioned",
    database_name="exampledb",
    master_username="admin",
    master_password=master_password,
    db_subnet_group_name=db_subnet_group.name,
    vpc_security_group_ids=[security_group.id],
    storage_encrypted=True,
    skip_final_snapshot=True,
    serverlessv2_scaling_configuration=rds.ClusterServerlessv2ScalingConfigurationArgs(
        max_capacity=1.0,
        min_capacity=0.5,
    ),
    tags={"Name": "aurora-example-cluster"}
)

# Create Aurora Instance
aurora_instance = rds.ClusterInstance("example-aurora-instance",
    identifier="aurora-example-instance-1",
    cluster_identifier=aurora_cluster.id,
    instance_class="db.serverless",
    engine=aurora_cluster.engine,
    engine_version=aurora_cluster.engine_version,
    tags={"Name": "aurora-example-instance"}
)

# Outputs
pulumi.export("cluster_endpoint", aurora_cluster.endpoint)
pulumi.export("cluster_port", aurora_cluster.port)
pulumi.export("database_name", aurora_cluster.database_name)