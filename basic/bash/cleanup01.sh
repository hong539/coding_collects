#!/bin/bash
# src: https://tldp.org/LDP/abs/html/sha-bang.html
# Cleanup
# Run as root, of course.

cd /var/log
cat /dev/null > messages
cat /dev/null > wtmp
echo "Log files cleaned up."