#!/bin/bash

cd DTaaS/deploy/docker
sudo docker-compose -f compose.local.yml --env-file .env.local down