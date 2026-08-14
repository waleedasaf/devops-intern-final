#!/usr/bin/env bash
#
# sysinfo.sh - Prints basic system information.
#
# Usage: ./scripts/sysinfo.sh

set -euo pipefail

echo "===== System Info ====="

echo -e "\n--- Current User ---"
whoami

echo -e "\n--- Current Date ---"
date

echo -e "\n--- Disk Usage ---"
df -h

echo -e "\n========================"
