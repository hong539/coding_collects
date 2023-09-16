#!/bin/bash

# 指定access.log文件的路径
log_file="access.log"

# 创建一个临时文件来存储排序后的数据
sorted_file=$(mktemp)

# 读取access.log文件并根据每行每列的内容进行排序
while IFS= read -r line; do
    # 使用awk将每行拆分成列，并以特定的分隔符排序（这里使用空格作为分隔符）
    sorted_line=$(echo "$line" | awk '{ for(i=1; i<=NF; i++) print $i }' | sort | tr '\n' '\t')
    echo "$sorted_line" >> "$sorted_file"
done < "$log_file"

# 输出表头
echo -e "IP\t-\t-\tTimestamp\tMethod\tURL\tProtocol\tStatus\tSize\t-\tUser-Agent\t-\tLatency\t-"

# 输出最小值行
min_line=$(sort -k14 -n "$sorted_file" | head -n 1)
echo -e "$min_line"

# 删除临时文件
rm -f "$sorted_file"