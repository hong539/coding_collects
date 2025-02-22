#!/usr/bin/env bash

# Function to print a usage message to stderr
usage() {
    printf "Usage: %s <person>\n" "$(basename "$0")" >&2
}

# Function to print a greeting message
greet() {
    local name="$1"
    printf "Hello, %s\n" "$name"
}

# Main function to handle argument validation
main() {
    if [[ $# -ne 1 ]]; then
        usage
        return 1
    fi

    greet "$1"
}

# Execute main with all arguments
main "$@"