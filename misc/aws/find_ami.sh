#!/bin/bash

set -euo pipefail

REGION="ap-northeast-1" # Tokyo region
AMI_NAME_PATTERN="al2023-ami" # Updated AMI name filter
AMI_DESCRIPTION_KEYWORD="Amazon Linux 2023" # Description keyword filter

find_ami() {
    local region="$1"
    local name_pattern="$2"
    local description_keyword="$3"
    local ami_info

    # Use AWS CLI to describe images and filter the results
    if ! ami_info=$(aws ec2 describe-images \
        --region "$region" \
        --owners "amazon" \
        --filters "Name=name,Values=*" "Name=state,Values=available" \
        --query "Images[?contains(Name, \`${name_pattern}\`) && contains(Description, \`${description_keyword}\`)].{AMI_ID:ImageId,Name:Name,Description:Description}" \
        --output json); then
        printf "Failed to retrieve AMI information from AWS.\n" >&2
        return 1
    fi

    # Validate output
    if [[ -z "$ami_info" || "$ami_info" == "[]" ]]; then
        printf "No matching AMIs found in region: %s with the specified criteria.\n" "$region" >&2
        return 1
    fi

    # Print filtered AMI details
    printf "Matching AMIs in region '%s':\n" "$region"
    printf "%s\n" "$ami_info" | jq -r '.[] | "AMI ID: \(.AMI_ID), Name: \(.Name), Description: \(.Description)"'
    return 0
}

main() {
    # Ensure jq and AWS CLI are installed
    if ! command -v aws > /dev/null || ! command -v jq > /dev/null; then
        printf "Required tools 'aws' or 'jq' are not installed. Please install them first.\n" >&2
        return 1
    fi

    find_ami "$REGION" "$AMI_NAME_PATTERN" "$AMI_DESCRIPTION_KEYWORD"
}

main "$@"