#!/bin/bash

# Step 1: Clone the repository
echo "Cloning the DTaaS repository..."
git clone https://github.com/INTO-CPS-Association/DTaaS
if [ $? -ne 0 ]; then
  echo "Failed to clone the repository. Exiting..."
  exit 1
fi

# Step 2: Install docker-compose
echo "Installing docker-compose..."
sudo apt install -y docker-compose
if [ $? -ne 0 ]; then
  echo "Failed to install docker-compose. Exiting..."
  exit 1
fi

# Step 3: Ask user for their GitLab username
echo "Enter your GitLab username:"
read username
cd DTaaS
pwd_val=$(pwd)

# Step 3.5: Change directory to deploy/docker
cp -R files/user1 files/${username}

# Step 4: Change directory to deploy/docker
cd deploy/docker || { echo "Directory not found. Exiting..."; exit 1; }

# Step 5: Update .env.local with the required values
echo "Updating .env.local with the correct values..."
sed -i "s|DTAAS_DIR=.*|DTAAS_DIR='${pwd_val}'|" .env.local
sed -i "s|username1=.*|username1='${username}'|" .env.local

