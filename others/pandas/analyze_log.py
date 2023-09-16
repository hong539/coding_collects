import pandas as pd

# 读取access.log文件到DataFrame
log_file = "access.log"
df = pd.read_csv(log_file, sep=' ', header=None)

# print(df)

# # 提取最后一列（延迟时间）并将其转换为浮点数
# df[13] = df[13].str.replace('-', '0').astype(float)

# # 根据最后一列的值进行排序
df_sorted = df.sort_values(by=[11])

print(df_sorted)

# # 显示DataFrame的第一行（最小值）
# min_row = df_sorted.iloc[0]

# print(min_row)

# # 输出最小值行
# print(min_row)