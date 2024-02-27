#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: pat <file>"
  exit 1
fi
cat $1 | python3 $PYTHON_SCRIPTS_PATH/cmds/cat-copy.py
