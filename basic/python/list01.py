# src: https://datagy.io/python-list-find-all-index/
# Using enumerate to Find Index Positions
a_list = [1,2,3,4,1,2,1,2,3,4]
def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(a_list):
        if value == item_to_find:
            indices.append(idx)
    return indices

print(find_indices(a_list, 1))

# Returns: [0, 4, 6]