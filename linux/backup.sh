#!/bin/bash

# CloudMatrix Backup Script

SOURCE="/etc"
BACKUP_DIR="$HOME/CloudMatrix_Backups"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/cloudmatrix_backup_$DATE.tar.gz"

echo "=========================================="
echo "CLOUDMATRIX BACKUP SYSTEM"
echo "=========================================="

mkdir -p "$BACKUP_DIR"

echo
echo "Backup source : $SOURCE"
echo "Backup folder : $BACKUP_DIR"

echo
echo "Creating backup..."

tar -czf "$BACKUP_FILE" "$SOURCE" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "Backup completed successfully."
    echo "Backup file: $BACKUP_FILE"
else
    echo "Backup completed with warnings."
    echo "Some files may require root privileges."
fi

echo
echo "Backup contents:"
ls -lh "$BACKUP_DIR"

echo
echo "=========================================="
echo "BACKUP PROCESS COMPLETED"
echo "=========================================="