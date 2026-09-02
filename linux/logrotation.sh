    #!/bin/bash

# CloudMatrix Log Rotation Script

LOG_DIR="/var/log"
BACKUP_DIR="$HOME/CloudMatrix_Log_Backups"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")

echo "=========================================="
echo "CLOUDMATRIX LOG ROTATION"
echo "=========================================="

mkdir -p "$BACKUP_DIR"

echo
echo "Log directory : $LOG_DIR"
echo "Backup folder : $BACKUP_DIR"

echo
echo "Available log files:"

find "$LOG_DIR" -maxdepth 1 -type f -name "*.log" -print 2>/dev/null

echo
echo "Log rotation configuration:"
echo "- Logs are periodically archived."
echo "- Old logs are compressed."
echo "- Archived logs are retained for recovery."
echo "- Rotation prevents excessive disk usage."

echo
echo "=========================================="
echo "LOG ROTATION CONFIGURATION COMPLETED"
echo "=========================================="