#!/bin/bash

# Check if a filename argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Assign the provided argument to a variable
FILE="$1"

# Check if the file exists
if [ -f "$FILE" ]; then
    echo "File '$FILE' exists. Here is its content:"
    cat "$FILE"
else
    echo "File '$FILE' does not exist."
fi
