#!/bin/bash

# Define the log file path
LOG_FILE="/var/log/syslog"  # Change this to your log file path if needed

# Define the output file
ERROR_LOG="error_messages.log"

# Extract lines containing "error" (case-insensitive) and save to output file
grep -i "error" "$LOG_FILE" > "$ERROR_LOG"

echo "✅ Extracted error messages from $LOG_FILE to $ERROR_LOG"
