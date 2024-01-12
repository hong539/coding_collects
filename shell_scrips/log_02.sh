#!/bin/bash

# 启用输出到stdout的日志
exec 3>&1

# 定义一个函数，用于输出日志
log() {
    local message="$1"
    echo "$(date '+%Y/%m/%d %H:%M:%S') $message" >&3
}

# 示例脚本，输出每一步的日志
log "Starting script..."

# 在这里添加你的脚本逻辑，每一步都调用log函数输出日志
log "Performing step 1..."
ls

log "Performing step 2..."
# 步骤2的实际命令

log "Performing step 3..."
# 步骤3的实际命令

# 结束脚本
log "Script completed."