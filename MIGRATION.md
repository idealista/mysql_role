# Migration Guide: From Ansible MySQL Role to Pulumi Aurora Serverless

This guide helps you migrate from the Ansible MySQL role to the new Pulumi-based Aurora Serverless deployment.

## Overview of Changes

| Aspect | Ansible Role | Pulumi Aurora Serverless |
|--------|-------------|-------------------------|
| **Infrastructure** | Local MySQL/MariaDB installation | AWS RDS Aurora Serverless v2 |
| **Scaling** | Manual server scaling | Automatic serverless scaling |
| **Availability** | Single instance | Multi-AZ with automatic failover |
| **Backups** | Manual configuration | Automated with point-in-time recovery |
| **Security** | Local firewall rules | VPC security groups + encryption |
| **Maintenance** | Manual updates | Managed by AWS |
| **Cost Model** | Fixed server costs | Pay-per-use serverless model |

## Migration Steps

### 1. Backup Existing Data (if applicable)

If you have existing MySQL data from the Ansible deployment:

```bash
# Create a backup of your existing MySQL database
mysqldump -u root -p --all-databases > mysql_backup.sql

# Or backup specific databases
mysqldump -u root -p database_name > database_backup.sql
```

### 2. Install Pulumi and Dependencies

```bash
# Install Pulumi CLI
curl -fsSL https://get.pulumi.com | sh

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Configure AWS Credentials

```bash
# Configure AWS CLI
aws configure

# Or set environment variables
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="us-east-1"
```

### 4. Initialize Pulumi Stack

```bash
# Initialize new stack
pulumi stack init production  # or dev, staging, etc.

# Set AWS region
pulumi config set aws:region us-east-1
```

### 5. Configure Database Settings

Map your Ansible variables to Pulumi configuration:

#### Ansible Variables → Pulumi Config

```bash
# Database name (from mysql_databases in Ansible)
pulumi config set rds-aurora-serverless:db_name "your_database_name"

# Master credentials (from mysql_root_user/mysql_root_password)
pulumi config set rds-aurora-serverless:master_username "root"
pulumi config set rds-aurora-serverless:master_password "your-secure-password" --secret

# Environment
pulumi config set rds-aurora-serverless:environment "production"

# Scaling configuration
pulumi config set rds-aurora-serverless:min_capacity 0.5
pulumi config set rds-aurora-serverless:max_capacity 4.0

# Security (restrict access)
pulumi config set rds-aurora-serverless:allowed_cidr_blocks '["10.0.0.0/8"]'

# Production settings
pulumi config set rds-aurora-serverless:deletion_protection true
pulumi config set rds-aurora-serverless:skip_final_snapshot false
pulumi config set rds-aurora-serverless:backup_retention_period 30
```

### 6. Deploy Aurora Serverless

```bash
# Preview the deployment
pulumi preview

# Deploy the infrastructure
pulumi up
```

### 7. Restore Data (if applicable)

After deployment, restore your data to the new Aurora cluster:

```bash
# Get connection details
ENDPOINT=$(pulumi stack output cluster_endpoint)
PORT=$(pulumi stack output cluster_port)
USERNAME=$(pulumi stack output master_username)
DATABASE=$(pulumi stack output database_name)

# Restore data
mysql -h $ENDPOINT -P $PORT -u $USERNAME -p$PASSWORD $DATABASE < mysql_backup.sql
```

### 8. Update Application Configuration

Update your applications to use the new Aurora endpoints:

```bash
# Get new connection details
pulumi stack output cluster_endpoint        # Write endpoint
pulumi stack output cluster_reader_endpoint # Read endpoint
pulumi stack output cluster_port           # Port (3306)
pulumi stack output connection_string      # Full connection string
```

## Configuration Mapping

### Ansible Role Variables → Pulumi Configuration

| Ansible Variable | Pulumi Config | Notes |
|-----------------|---------------|-------|
| `mysql_root_user` | `master_username` | Database master user |
| `mysql_root_password` | `master_password` | Use `--secret` flag |
| `mysql_databases[].name` | `db_name` | Primary database name |
| `mysql_global_variables.mysqld.port` | Fixed at 3306 | Aurora standard port |
| `mysql_global_variables.mysqld.bind_address` | Managed by VPC | Network access via security groups |
| `mysql_global_variables.mysqld.max_connections` | `max_capacity` | Scales automatically |
| `mysql_service_enabled` | Always enabled | Managed service |
| `mysql_service_state` | Always running | Serverless auto-pause |

### Database Configuration

Aurora Serverless automatically manages many MySQL configurations that were manual in the Ansible role:

- **Buffer Pool Size**: Automatically sized based on instance capacity
- **Connection Limits**: Scales with capacity
- **Log Files**: Managed by CloudWatch
- **Backup Settings**: Automated with configurable retention

## Network and Security Changes

### Ansible Role Security
```yaml
# Ansible: Local firewall rules
mysql_global_variables:
  mysqld:
    bind_address: 0.0.0.0  # or specific IP
```

### Pulumi Security
```bash
# Pulumi: VPC Security Groups
pulumi config set rds-aurora-serverless:allowed_cidr_blocks '["10.0.0.0/16","172.16.0.0/12"]'
```

## Monitoring and Logging

### Ansible Role
- Manual log configuration
- Local log files
- Custom monitoring setup

### Aurora Serverless
- Automatic CloudWatch integration
- Performance Insights available
- Enhanced monitoring options

Enable enhanced monitoring:
```python
# In __main__.py, add to cluster configuration:
monitoring_interval=60,
enabled_cloudwatch_logs_exports=["error", "general", "slow-query"],
```

## Cost Optimization

### Ansible Role Costs
- Fixed server costs (24/7)
- Manual scaling
- Infrastructure maintenance

### Aurora Serverless Costs
- Pay-per-use (scales to zero)
- Automatic scaling
- No infrastructure maintenance

Configure cost-effective scaling:
```bash
# Development environment
pulumi config set rds-aurora-serverless:min_capacity 0.5
pulumi config set rds-aurora-serverless:max_capacity 1.0

# Production environment
pulumi config set rds-aurora-serverless:min_capacity 1.0
pulumi config set rds-aurora-serverless:max_capacity 16.0
```

## Rollback Plan

If you need to rollback to the Ansible deployment:

1. **Backup Aurora data**:
```bash
mysqldump -h $(pulumi stack output cluster_endpoint) -u $(pulumi stack output master_username) -p --all-databases > aurora_backup.sql
```

2. **Keep Ansible playbooks** (don't delete until migration is confirmed successful)

3. **Destroy Pulumi stack** (only after confirming rollback):
```bash
pulumi destroy
```

## Testing the Migration

1. **Connectivity Test**:
```bash
mysql -h $(pulumi stack output cluster_endpoint) -P $(pulumi stack output cluster_port) -u $(pulumi stack output master_username) -p
```

2. **Performance Test**:
```bash
# Run your application's database tests
# Monitor Aurora metrics in CloudWatch
```

3. **Scaling Test**:
```bash
# Generate load to test auto-scaling
# Monitor capacity changes in AWS console
```

## Troubleshooting

### Common Issues

1. **Connection Timeouts**:
   - Check security group rules
   - Verify VPC configuration
   - Ensure subnets span multiple AZs

2. **Authentication Failures**:
   - Verify master password configuration
   - Check username format
   - Ensure SSL/TLS settings

3. **Performance Issues**:
   - Adjust min/max capacity settings
   - Enable Performance Insights
   - Review CloudWatch metrics

### Getting Help

- Check Pulumi logs: `pulumi logs`
- View AWS CloudWatch logs
- Monitor Aurora metrics in AWS Console
- Review VPC Flow Logs for network issues

## Post-Migration Cleanup

After successful migration and testing:

1. **Remove Ansible files** (backup first):
```bash
# Backup old files
tar -czf ansible-mysql-backup.tar.gz tasks/ vars/ templates/ defaults/

# Remove Ansible-specific files
rm -rf tasks/ vars/ templates/ defaults/ meta/
```

2. **Update documentation**
3. **Update CI/CD pipelines**
4. **Train team on new Pulumi workflow**

## Benefits Realized

After migration, you'll benefit from:

- **Reduced operational overhead**: No server maintenance
- **Automatic scaling**: Handles traffic spikes automatically  
- **High availability**: Multi-AZ deployment with automatic failover
- **Enhanced security**: VPC isolation and encryption
- **Cost optimization**: Pay only for actual usage
- **Managed backups**: Automated with point-in-time recovery
- **Infrastructure as Code**: Version-controlled infrastructure