#!/bin/bash

# Define log directory
LOG_DIR="/var/log"

# Find and delete log files older than 7 days
find "$LOG_DIR" -type f -name "*.log" -mtime +7 -exec rm -f {} \;

# Print success message
echo "✅ Deleted log files older than 7 days from $LOG_DIR"
