#!/bin/bash
set -euo pipefail
aws ec2 describe-images \
    --region ap-northeast-1 \
    --owners "amazon" \
    --filters "Name=name,Values=*" "Name=state,Values=available" \
    --query 'Images[?Name != `null` && contains(Name, `al2023-ami`) && contains(Name, `x86_64`) && contains(Description, `Amazon Linux 2023`)].{AMI_ID:ImageId,Name:Name,Description:Description}' \
    --output json