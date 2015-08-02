#!/usr/bin/env bash

pkill -f 'security_camera_server'
until python security_camera_server.py; do
    echo "Server 'myserver' crashed with exit code $?.  Respawning.." >&2
    sleep 1
    pkill -f 'security_camera_server'
done
