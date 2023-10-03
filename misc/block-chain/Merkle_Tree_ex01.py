import hashlib

def merkle_tree(txns):
    if len(txns) % 2 != 0:
        txns.append(txns[-1])
    tree = []
    for i in range(0, len(txns), 2):
        pair = txns[i:i+2]
        pair_hash = hashlib.sha256(pair[0].encode() + pair[1].encode()).hexdigest()
        tree.append(pair_hash)
    if len(tree) == 1:
        return tree[0]
    else:
        return merkle_tree(tree)