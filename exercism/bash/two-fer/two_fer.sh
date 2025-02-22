#!/usr/bin/env bash

# The following comments should help you get started:
# - Bash is flexible. You may use functions or write a "raw" script.
#
# - Complex code can be made easier to read by breaking it up
#   into functions, however this is sometimes overkill in bash.
#
# - You can find links about good style and other resources
#   for Bash in './README.md'. It came with this exercise.
#
# Function to determine the cookie-sharing message
share_cookie() {
    local recipient="${1:-you}"
    printf "One for %s, one for me.\n" "$recipient"
}

# Main function
main() {
    share_cookie "${1:-}"
}

# Execute main with all arguments
main "$@"
