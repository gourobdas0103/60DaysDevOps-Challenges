#!/bin/bash

# Define the website URL
WEBSITE="https://www.learnxops.com"

# Check website reachability using curl
if curl -Is "$WEBSITE" | head -n 1 | grep -q "200\|301\|302"; then
    echo "✅ $WEBSITE is reachable via curl."
else
    echo "❌ $WEBSITE is not reachable via curl."
fi

# Extract domain from URL for ping
DOMAIN=$(echo $WEBSITE | awk -F/ '{print $3}')

# Check reachability using ping (send 1 packet, wait max 2 sec)
if ping -c 1 -W 2 "$DOMAIN" &>/dev/null; then
    echo "✅ $DOMAIN is reachable via ping."
else
    echo "❌ $DOMAIN is not reachable via ping."
fi
