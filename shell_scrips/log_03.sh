#!/bin/bash
# src: https://serverfault.com/questions/310098/how-to-add-a-timestamp-to-bash-script-log
adddate() {
    while IFS= read -r line; do
        printf '%s %s\n' "$(date +"%Y-%m-%d %H:%M:%S")" "$line";
    done
}

{
    echo "This is a sample line 1"
    echo "This is a sample line 2"
    echo "This is a sample line 3"
} | adddate >> ./test.log