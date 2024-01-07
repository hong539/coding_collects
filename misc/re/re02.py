import re

# Sample text data
text_data = """
→ s32244153: [はらヘリ堂 (ヘリを)] シスターマーガレットの受難 12/31 22:21
→ s32244153: [Noir Complex (NR)] 指揮官と面談する 12/31 22:21
→ s32244153: [瓦屋工房 (瓦爺)] なんでVtuber風俗にクレアさんが!? 12/31 22:22
→ s32244153: [キレイナブタ (ぶたちゃんぐ)] 異世界の女たち 5.0 12/31 22:22
... (other lines)
"""

# Splitting the text into lines
lines = text_data.split('\n')

# Pattern to match the prefix and the timestamp at the end
pattern = r'^→ s32244153: | \d{2}:\d{2}$'

# Processing each line to remove the prefix and timestamp
processed_lines = [re.sub(pattern, '', line) for line in lines]

# Joining the processed lines back into text
processed_text = '\n'.join(processed_lines)

# Displaying the processed text
print(processed_text)