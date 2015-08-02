#!/usr/bin/env bash

until python security_camera_server.py; do
    echo "Server 'myserver' crashed with exit code $?.  Respawning.." >&2
    sleep 1
done
