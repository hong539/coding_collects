import hashlib

def proof_of_work(block, difficulty):
    target = '0' * difficulty
    nonce = 0
    while True:
        data = f'{block}{nonce}'.encode()
        hash_value = hashlib.sha256(data).hexdigest()
        if hash_value[:difficulty] == target:
            return nonce
        nonce += 1