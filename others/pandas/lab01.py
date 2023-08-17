import pandas as pd

df = pd.read_csv('./test_data/test.csv')
grouped = df.groupby("name")

with open('output', 'w') as f:
    for name, group in grouped:
        group.drop('name', axis=1, inplace=True)
        print(f"group = {name}", file=f)
        print("{", file=f)
        
        for col in group.columns:
            print(f"s_name {col}=", end="", file=f)
            print(f"{' and ' .join(group[col].astype(str))}", file=f)

        print("}",)