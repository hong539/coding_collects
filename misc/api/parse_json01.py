import json
import pandas as pd

# JSON data
json_data = '{"data": {"group": {"id": "gid://gitlab/Group/12345678", "name": "group-name", "projects": {"nodes": [{"name": "repo01"}, {"name": "repo02"}]}}}}'

# Convert JSON to Python dictionary
data = json.loads(json_data)

# Extract the 'nodes' list from the 'projects' dictionary
nodes = data['data']['group']['projects']['nodes']

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(nodes)

# Print DataFrame
print(df)