#!/usr/bin/env bash
# Detect WSL2 IP and update frontend connection

# 1. Get WSL2 IP
WSL_IP=$(ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1)

if [ -z "$WSL_IP" ]; then
  echo "Could not detect WSL IP."
  exit 1
fi

echo "Detected WSL IP: $WSL_IP"

# 2. Update frontend JSX file
FRONTEND_FILE="./web/src/GMPanel.jsx"

# Use sed to replace the io(...) line
sed -i "s#const socket = io(.*);#const socket = io(\"http://$WSL_IP:3001\");#" "$FRONTEND_FILE"

echo "Frontend socket address updated."
