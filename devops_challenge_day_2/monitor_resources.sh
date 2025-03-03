#!/bin/bash

# Define log file
LOG_FILE="resource_monitor.log"

# Print header
echo "Monitoring CPU and Memory Usage - Logging to $LOG_FILE"
echo "Timestamp       | CPU Usage (%) | Memory Usage (%)" > "$LOG_FILE"

# Continuous monitoring every 5 seconds
while true; do
    # Get current timestamp
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

    # Get CPU usage (ignoring idle %)
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}')

    # Get Memory usage percentage
    MEM_USAGE=$(free | awk '/Mem/ {printf "%.2f", $3/$2 * 100}')

    # Log data
    echo "$TIMESTAMP | $CPU_USAGE%         | $MEM_USAGE%" >> "$LOG_FILE"

    # Wait 5 seconds before next check
    sleep 5
done
