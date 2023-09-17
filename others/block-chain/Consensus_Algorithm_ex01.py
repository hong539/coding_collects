import random

# 创建一个包含节点的列表
nodes = ["Node A", "Node B", "Node C"]

# 模拟每个节点提出不同的候选值
candidate_values = {node: random.randint(1, 100) for node in nodes}

# 打印每个节点提出的候选值
for node, value in candidate_values.items():
    print(f"{node}: Candidate Value = {value}")

# 使用投票算法选择最终共识值
consensus_value = max(candidate_values, key=candidate_values.get)

# 打印最终共识值
print(f"Consensus Value: {consensus_value}")