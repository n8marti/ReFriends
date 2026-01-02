#!/usr/bin/env bash

usage="$0 [USER@]DEST [NAME]
Connect to DEST (IP or domain name) with detachable SSH session via screen.
If NAME is not given \"default\" is used for the session name."

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "$usage"
    exit 0
fi
# Connect via ssh to screen at destination to allow sessions to be detachable.
ssh -t "$1" screen -d -R "${2:-default}"
