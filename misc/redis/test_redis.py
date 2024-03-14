import redis

# Connect to Redis
redis_host = 'localhost'  # Replace with your Redis server host
redis_port = 6379  # Replace with your Redis server port
redis_db = 0  # Replace with your Redis database number if necessary
redis_password = None  # Replace with your Redis password if necessary

# Connect to Redis server
redis_client = redis.StrictRedis(
    host=redis_host,
    port=redis_port,
    db=redis_db,
    password=redis_password,
    decode_responses=True  # Automatically decode responses to strings
)

# Define the value to search for
value_to_search = "special values"

# Iterate over all keys and search for the value
keys = redis_client.keys("*")  # Get all keys in the database

for key in keys:
    value = redis_client.get(key)
    if value == value_to_search:
        print(f"Value '{value_to_search}' found in key '{key}'")