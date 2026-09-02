#!/bin/bash

echo "=========================================="
echo "CLOUDMATRIX USER MANAGEMENT"
echo "=========================================="

# Check whether script is running with root privileges
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script using sudo."
    exit 1
fi

echo
echo "--- Creating CloudMatrix users ---"

# Create users if they do not already exist
for user in cloudadmin clouduser1 clouduser2; do

    if id "$user" >/dev/null 2>&1; then
        echo "User '$user' already exists."
    else
        useradd -m "$user"
        echo "User '$user' created."
    fi

done

echo
echo "--- User Information ---"

for user in cloudadmin clouduser1 clouduser2; do
    id "$user"
    echo
done

echo "--- Home Directories ---"

ls -ld /home/cloudadmin
ls -ld /home/clouduser1
ls -ld /home/clouduser2

echo
echo "=========================================="
echo "USER MANAGEMENT COMPLETED"
echo "=========================================="

