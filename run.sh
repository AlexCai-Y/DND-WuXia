#!/usr/bin/env bash
set -e

echo "Updating frontend with WSL IP..."
./update_ip.sh

echo "Starting backend..."
( cd game && python3 main.py ) &

echo "Starting frontend..."
( cd web && npm install && npm run dev ) &

wait