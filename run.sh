#!/bin/sh

FILE="$1"
[ ! -f "$FILE" ] && echo "Error: File inputted, \"$FILE\", doesn't exist." && exit 1

env $(cat "$FILE" | xargs) $(dirname "$0")/build/watch-sync
