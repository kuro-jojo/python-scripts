#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: pat <file>"
  exit 1
fi
cat $1 | python3 cat-copy.py