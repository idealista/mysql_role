# Basic Aurora Serverless Example

This example demonstrates the minimal configuration needed to deploy an Aurora Serverless v2 MySQL cluster.

## Usage

1. Navigate to this directory:
```bash
cd examples/basic
```

2. Install dependencies:
```bash
pip install pulumi pulumi-aws
```

3. Initialize Pulumi stack:
```bash
pulumi stack init dev
```

4. Set the required password:
```bash
pulumi config set master_password "your-secure-password" --secret
```

5. Deploy:
```bash
pulumi up
```

## What this creates

- Aurora Serverless v2 MySQL cluster
- Uses default VPC and subnets
- Basic security group allowing MySQL access
- Minimal scaling configuration (0.5-1.0 ACU)

## Connecting

After deployment, connect using:
```bash
mysql -h $(pulumi stack output cluster_endpoint) -P $(pulumi stack output cluster_port) -u admin -p$(pulumi config get master_password) $(pulumi stack output database_name)
```