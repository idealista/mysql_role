"""
RDS Aurora Serverless deployment using Pulumi
Replaces the MySQL Ansible role with cloud-native Aurora Serverless
"""

import pulumi
import pulumi_aws as aws
from pulumi_aws import rds, ec2
import json

# Get configuration
config = pulumi.Config()
aws_config = pulumi.Config("aws")

# Configuration with defaults based on the original Ansible role
db_name = config.get("db_name") or "mysql"
master_username = config.get("master_username") or "root"
master_password = config.get("master_password") or "default"
engine_version = config.get("engine_version") or "8.0.mysql_aurora.3.02.0"
backup_retention_period = config.get_int("backup_retention_period") or 7
preferred_backup_window = config.get("preferred_backup_window") or "03:00-04:00"
preferred_maintenance_window = config.get("preferred_maintenance_window") or "sun:04:00-sun:05:00"
deletion_protection = config.get_bool("deletion_protection") or False
skip_final_snapshot = config.get_bool("skip_final_snapshot") or True

# VPC and Security Group configuration
vpc_cidr = config.get("vpc_cidr") or "10.0.0.0/16"
allowed_cidr_blocks = config.get_object("allowed_cidr_blocks") or ["0.0.0.0/0"]

# Create VPC if not provided
vpc_id = config.get("vpc_id")
if not vpc_id:
    # Create VPC
    vpc = ec2.Vpc("aurora-vpc",
        cidr_block=vpc_cidr,
        enable_dns_hostnames=True,
        enable_dns_support=True,
        tags={
            "Name": "aurora-serverless-vpc",
            "Environment": config.get("environment") or "dev"
        }
    )
    vpc_id = vpc.id
    
    # Create Internet Gateway
    igw = ec2.InternetGateway("aurora-igw",
        vpc_id=vpc.id,
        tags={
            "Name": "aurora-serverless-igw"
        }
    )
    
    # Create public subnets in different AZs
    availability_zones = aws.get_availability_zones(state="available")
    
    public_subnet_1 = ec2.Subnet("aurora-public-subnet-1",
        vpc_id=vpc.id,
        cidr_block="10.0.1.0/24",
        availability_zone=availability_zones.names[0],
        map_public_ip_on_launch=True,
        tags={
            "Name": "aurora-serverless-public-subnet-1"
        }
    )
    
    public_subnet_2 = ec2.Subnet("aurora-public-subnet-2",
        vpc_id=vpc.id,
        cidr_block="10.0.2.0/24",
        availability_zone=availability_zones.names[1],
        map_public_ip_on_launch=True,
        tags={
            "Name": "aurora-serverless-public-subnet-2"
        }
    )
    
    # Create private subnets for RDS
    private_subnet_1 = ec2.Subnet("aurora-private-subnet-1",
        vpc_id=vpc.id,
        cidr_block="10.0.10.0/24",
        availability_zone=availability_zones.names[0],
        tags={
            "Name": "aurora-serverless-private-subnet-1"
        }
    )
    
    private_subnet_2 = ec2.Subnet("aurora-private-subnet-2",
        vpc_id=vpc.id,
        cidr_block="10.0.11.0/24",
        availability_zone=availability_zones.names[1],
        tags={
            "Name": "aurora-serverless-private-subnet-2"
        }
    )
    
    # Create route table for public subnets
    public_route_table = ec2.RouteTable("aurora-public-rt",
        vpc_id=vpc.id,
        tags={
            "Name": "aurora-serverless-public-rt"
        }
    )
    
    # Create route to internet gateway
    public_route = ec2.Route("aurora-public-route",
        route_table_id=public_route_table.id,
        destination_cidr_block="0.0.0.0/0",
        gateway_id=igw.id
    )
    
    # Associate public subnets with route table
    public_rta_1 = ec2.RouteTableAssociation("aurora-public-rta-1",
        subnet_id=public_subnet_1.id,
        route_table_id=public_route_table.id
    )
    
    public_rta_2 = ec2.RouteTableAssociation("aurora-public-rta-2",
        subnet_id=public_subnet_2.id,
        route_table_id=public_route_table.id
    )
    
    subnet_ids = [private_subnet_1.id, private_subnet_2.id]
else:
    # Use existing VPC - get subnets
    vpc = ec2.get_vpc(id=vpc_id)
    subnets = ec2.get_subnets(filters=[
        {"name": "vpc-id", "values": [vpc_id]}
    ])
    subnet_ids = subnets.ids

# Create DB Subnet Group
db_subnet_group = rds.SubnetGroup("aurora-subnet-group",
    subnet_ids=subnet_ids,
    tags={
        "Name": "aurora-serverless-subnet-group",
        "Environment": config.get("environment") or "dev"
    }
)

# Create Security Group for Aurora
security_group = ec2.SecurityGroup("aurora-security-group",
    name="aurora-serverless-sg",
    description="Security group for Aurora Serverless cluster",
    vpc_id=vpc_id,
    ingress=[
        ec2.SecurityGroupIngressArgs(
            description="MySQL/Aurora",
            from_port=3306,
            to_port=3306,
            protocol="tcp",
            cidr_blocks=allowed_cidr_blocks,
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
    tags={
        "Name": "aurora-serverless-security-group",
        "Environment": config.get("environment") or "dev"
    }
)

# Create Aurora Serverless v2 Cluster
aurora_cluster = rds.Cluster("aurora-serverless-cluster",
    cluster_identifier=config.get("cluster_identifier") or "aurora-serverless-mysql",
    engine="aurora-mysql",
    engine_version=engine_version,
    engine_mode="provisioned",  # Aurora Serverless v2 uses provisioned mode
    database_name=db_name,
    master_username=master_username,
    master_password=master_password,
    backup_retention_period=backup_retention_period,
    preferred_backup_window=preferred_backup_window,
    preferred_maintenance_window=preferred_maintenance_window,
    db_subnet_group_name=db_subnet_group.name,
    vpc_security_group_ids=[security_group.id],
    storage_encrypted=True,
    deletion_protection=deletion_protection,
    skip_final_snapshot=skip_final_snapshot,
    final_snapshot_identifier=f"aurora-serverless-final-snapshot-{pulumi.get_stack()}",
    # Serverless v2 scaling configuration
    serverlessv2_scaling_configuration=rds.ClusterServerlessv2ScalingConfigurationArgs(
        max_capacity=config.get_float("max_capacity") or 1.0,
        min_capacity=config.get_float("min_capacity") or 0.5,
    ),
    tags={
        "Name": "aurora-serverless-cluster",
        "Environment": config.get("environment") or "dev",
        "ManagedBy": "Pulumi"
    }
)

# Create Aurora Serverless v2 Instance
aurora_instance = rds.ClusterInstance("aurora-serverless-instance",
    identifier=config.get("instance_identifier") or "aurora-serverless-instance-1",
    cluster_identifier=aurora_cluster.id,
    instance_class="db.serverless",  # Serverless v2 instance class
    engine=aurora_cluster.engine,
    engine_version=aurora_cluster.engine_version,
    tags={
        "Name": "aurora-serverless-instance",
        "Environment": config.get("environment") or "dev",
        "ManagedBy": "Pulumi"
    }
)

# Create Parameter Group (optional, for custom configurations)
parameter_group = rds.ParameterGroup("aurora-parameter-group",
    family="aurora-mysql8.0",
    description="Parameter group for Aurora Serverless MySQL",
    parameters=[
        rds.ParameterGroupParameterArgs(
            name="innodb_buffer_pool_size",
            value="{DBInstanceClassMemory*3/4}",
        ),
        rds.ParameterGroupParameterArgs(
            name="max_connections",
            value="151",
        ),
        rds.ParameterGroupParameterArgs(
            name="wait_timeout",
            value="28800",
        ),
    ],
    tags={
        "Name": "aurora-serverless-parameter-group",
        "Environment": config.get("environment") or "dev"
    }
)

# Outputs
pulumi.export("cluster_endpoint", aurora_cluster.endpoint)
pulumi.export("cluster_reader_endpoint", aurora_cluster.reader_endpoint)
pulumi.export("cluster_port", aurora_cluster.port)
pulumi.export("cluster_id", aurora_cluster.id)
pulumi.export("cluster_arn", aurora_cluster.arn)
pulumi.export("database_name", aurora_cluster.database_name)
pulumi.export("master_username", aurora_cluster.master_username)
pulumi.export("security_group_id", security_group.id)
pulumi.export("vpc_id", vpc_id)
pulumi.export("subnet_group_name", db_subnet_group.name)

# Connection information
pulumi.export("connection_string", pulumi.Output.concat(
    "mysql://", 
    aurora_cluster.master_username, 
    ":", 
    master_password,
    "@", 
    aurora_cluster.endpoint, 
    ":", 
    aurora_cluster.port, 
    "/", 
    aurora_cluster.database_name
))