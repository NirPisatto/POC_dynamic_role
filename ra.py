import redis
import time

# Connect to Redis server
redis_host = 'localhost'
redis_port = 6379
# redis_password = 'password'  # Add your password here if you have one

# Create a Redis connection
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

# Set a value in Redis
r.set('test_key', 'Hello Redis!')

# Get a value from Redis
last_time = time.time()
value = r.get('test_key')
print("Extract [redis]: ", time.time() - last_time)
print(value)
