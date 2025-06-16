# RDS Aurora Serverless Pulumi Project

This Pulumi project deploys an AWS RDS Aurora Serverless v2 MySQL database cluster, replacing the previous Ansible role for MySQL installation.

## Overview

This project creates:
- AWS RDS Aurora Serverless v2 MySQL cluster
- VPC with public and private subnets (if not provided)
- Security groups with MySQL access
- DB subnet group for multi-AZ deployment
- Parameter group for custom MySQL configurations

## Prerequisites

- [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/) installed
- [AWS CLI](https://aws.amazon.com/cli/) configured with appropriate credentials
- Python 3.7+ installed

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Configure your AWS credentials:
```bash
aws configure
```

3. Initialize Pulumi stack:
```bash
pulumi stack init dev
```

## Configuration

The project supports the following configuration options:

### Required Configuration
- `master_password`: Master password for the database (default: "changeme123!")

### Optional Configuration
- `db_name`: Database name (default: "mysql")
- `master_username`: Master username (default: "root")
- `environment`: Environment tag (default: "dev")
- `min_capacity`: Minimum Aurora Serverless capacity (default: 0.5)
- `max_capacity`: Maximum Aurora Serverless capacity (default: 1.0)
- `vpc_id`: Existing VPC ID (if not provided, creates new VPC)
- `vpc_cidr`: CIDR block for new VPC (default: "10.0.0.0/16")
- `allowed_cidr_blocks`: CIDR blocks allowed to access the database
- `backup_retention_period`: Backup retention in days (default: 7)
- `deletion_protection`: Enable deletion protection (default: false)
- `skip_final_snapshot`: Skip final snapshot on deletion (default: true)

### Setting Configuration

```bash
# Set required password
pulumi config set rds-aurora-serverless:master_password "your-secure-password" --secret

# Set optional configurations
pulumi config set rds-aurora-serverless:environment "production"
pulumi config set rds-aurora-serverless:min_capacity 1.0
pulumi config set rds-aurora-serverless:max_capacity 4.0
pulumi config set rds-aurora-serverless:deletion_protection true
```

## Deployment

1. Preview the deployment:
```bash
pulumi preview
```

2. Deploy the infrastructure:
```bash
pulumi up
```

3. View the outputs:
```bash
pulumi stack output
```

## Usage

After deployment, you can connect to your Aurora Serverless cluster using the provided endpoints:

```bash
# Get connection information
pulumi stack output cluster_endpoint
pulumi stack output cluster_port
pulumi stack output master_username
```

### Connecting with MySQL client

```bash
mysql -h $(pulumi stack output cluster_endpoint) \
      -P $(pulumi stack output cluster_port) \
      -u $(pulumi stack output master_username) \
      -p$(pulumi config get rds-aurora-serverless:master_password) \
      $(pulumi stack output database_name)
```

## Migration from Ansible Role

This Pulumi project replaces the previous Ansible MySQL role with the following improvements:

### Original Ansible Role Features → Pulumi Equivalent

| Ansible Role Feature | Pulumi Implementation |
|---------------------|----------------------|
| MySQL/MariaDB installation | RDS Aurora Serverless v2 MySQL |
| Local database configuration | Cloud-native managed service |
| User management | IAM and database users (can be extended) |
| Database creation | Automated through RDS |
| Service management | Fully managed by AWS |
| Configuration templates | Parameter groups |
| Security configuration | VPC security groups |

### Benefits of Aurora Serverless

- **Automatic scaling**: Scales compute capacity based on demand
- **Pay-per-use**: Only pay for resources when database is active
- **High availability**: Multi-AZ deployment with automatic failover
- **Managed backups**: Automated backups and point-in-time recovery
- **Security**: Encryption at rest and in transit
- **Monitoring**: CloudWatch integration for metrics and logs

## Outputs

The stack provides the following outputs:

- `cluster_endpoint`: Primary endpoint for write operations
- `cluster_reader_endpoint`: Reader endpoint for read operations
- `cluster_port`: Database port (3306)
- `cluster_id`: Aurora cluster identifier
- `cluster_arn`: Aurora cluster ARN
- `database_name`: Default database name
- `master_username`: Master username
- `security_group_id`: Security group ID
- `vpc_id`: VPC ID
- `subnet_group_name`: DB subnet group name
- `connection_string`: Full connection string

## Cleanup

To destroy the infrastructure:

```bash
pulumi destroy
```

## Security Considerations

1. **Password Management**: Use Pulumi secrets for sensitive data:
   ```bash
   pulumi config set rds-aurora-serverless:master_password "password" --secret
   ```

2. **Network Access**: Restrict `allowed_cidr_blocks` to specific IP ranges:
   ```bash
   pulumi config set rds-aurora-serverless:allowed_cidr_blocks '["10.0.0.0/8","172.16.0.0/12"]'
   ```

3. **Deletion Protection**: Enable for production environments:
   ```bash
   pulumi config set rds-aurora-serverless:deletion_protection true
   ```

## Troubleshooting

### Common Issues

1. **VPC Limits**: Ensure you have available VPCs in your region
2. **Subnet Availability**: Verify subnets exist in multiple AZs
3. **IAM Permissions**: Ensure your AWS credentials have RDS permissions
4. **Region Support**: Aurora Serverless v2 is not available in all regions

### Useful Commands

```bash
# Check stack status
pulumi stack

# View configuration
pulumi config

# Export stack state
pulumi stack export

# View logs
pulumi logs
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the deployment
5. Submit a pull request

## License

This project maintains the same Apache 2.0 license as the original Ansible role.