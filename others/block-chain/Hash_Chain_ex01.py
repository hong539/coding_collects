import hashlib

def hash_chain(n: int, data: str) -> str:
    """
    Generate a hash chain of length n starting with data.
    """
    hash_value = hashlib.sha256(data.encode()).hexdigest()
    for i in range(n - 1):
        hash_value = hashlib.sha256(hash_value.encode()).hexdigest()
    return hash_value

# Example usage
print(hash_chain(5, "hello world"))