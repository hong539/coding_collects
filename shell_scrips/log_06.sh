#!/bin/bash

# 使用awk为每一行添加时间戳
awk '{ print strftime("%Y/%m/%d %H:%M:%S"), $0 }'

echo "This is a sample line 1"
echo "This is a sample line 2"
echo "This is a sample line 3"