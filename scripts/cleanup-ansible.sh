#!/bin/bash

# Cleanup script for migrating from Ansible MySQL role to Pulumi Aurora Serverless
# This script backs up and removes Ansible-specific files

set -e

echo "🔄 Starting cleanup of Ansible MySQL role files..."

# Create backup directory with timestamp
BACKUP_DIR="ansible-backup-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo "📦 Creating backup in $BACKUP_DIR..."

# Backup Ansible files
if [ -d "tasks" ]; then
    cp -r tasks "$BACKUP_DIR/"
    echo "✅ Backed up tasks/"
fi

if [ -d "vars" ]; then
    cp -r vars "$BACKUP_DIR/"
    echo "✅ Backed up vars/"
fi

if [ -d "templates" ]; then
    cp -r templates "$BACKUP_DIR/"
    echo "✅ Backed up templates/"
fi

if [ -d "defaults" ]; then
    cp -r defaults "$BACKUP_DIR/"
    echo "✅ Backed up defaults/"
fi

if [ -d "meta" ]; then
    cp -r meta "$BACKUP_DIR/"
    echo "✅ Backed up meta/"
fi

if [ -d "handlers" ]; then
    cp -r handlers "$BACKUP_DIR/"
    echo "✅ Backed up handlers/"
fi

if [ -d "files" ]; then
    cp -r files "$BACKUP_DIR/"
    echo "✅ Backed up files/"
fi

# Backup other Ansible-specific files
for file in molecule.yml .yamllint .ansible-lint test-requirements.txt; do
    if [ -f "$file" ]; then
        cp "$file" "$BACKUP_DIR/"
        echo "✅ Backed up $file"
    fi
done

# Create compressed backup
tar -czf "${BACKUP_DIR}.tar.gz" "$BACKUP_DIR"
echo "📦 Created compressed backup: ${BACKUP_DIR}.tar.gz"

# Ask for confirmation before deletion
echo ""
echo "⚠️  Ready to remove Ansible files. This action cannot be undone!"
echo "   Backup created: ${BACKUP_DIR}.tar.gz"
echo ""
read -p "Do you want to proceed with deletion? (y/N): " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🗑️  Removing Ansible files..."
    
    # Remove Ansible directories
    for dir in tasks vars templates defaults meta handlers files molecule; do
        if [ -d "$dir" ]; then
            rm -rf "$dir"
            echo "✅ Removed $dir/"
        fi
    done
    
    # Remove Ansible-specific files
    for file in molecule.yml .yamllint .ansible-lint test-requirements.txt; do
        if [ -f "$file" ]; then
            rm "$file"
            echo "✅ Removed $file"
        fi
    done
    
    # Remove temporary backup directory (keep compressed version)
    rm -rf "$BACKUP_DIR"
    
    echo ""
    echo "🎉 Cleanup completed successfully!"
    echo "   Ansible files have been removed"
    echo "   Backup available at: ${BACKUP_DIR}.tar.gz"
    echo ""
    echo "📋 Next steps:"
    echo "   1. Initialize Pulumi stack: pulumi stack init <env>"
    echo "   2. Configure settings: pulumi config set rds-aurora-serverless:master_password <password> --secret"
    echo "   3. Deploy: pulumi up"
    echo "   4. See MIGRATION.md for detailed instructions"
    
else
    echo "❌ Cleanup cancelled. Ansible files preserved."
    echo "   Backup still available at: ${BACKUP_DIR}.tar.gz"
    rm -rf "$BACKUP_DIR"
fi

echo ""
echo "🔗 Useful commands:"
echo "   pulumi preview  # Preview changes"
echo "   pulumi up       # Deploy infrastructure"
echo "   pulumi destroy  # Remove infrastructure"
echo "   pulumi stack output  # View outputs"