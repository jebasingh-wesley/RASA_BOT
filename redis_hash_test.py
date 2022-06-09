import redis

# Create a redis client

redisClient = redis.StrictRedis(host='localhost',

                                port=6379,

                                db=0)

# Add key value pairs to the Redis hash

redisClient.hset("Cloud_Accounts", "GCP_1643565819_QATeam", "61f6d306abd0dd301b3a403e")

redisClient.hset("Cloud_Accounts", "AWS_940309581042_QATeam", "61f6cd72abd0dd301b3a3f67")

redisClient.hset("Cloud_Accounts", "CL_SaaS_QA_AUTOMATION_Acct", "61f6cefbabd0dd301b3a3f9d")

# Retrieve the value for a specific key

print("Value for the key AWS_940309581042_QATeam is")

print(redisClient.hget("Cloud_Accounts", "AWS_940309581042_QATeam"))

print("The keys present in the Redis hash:");

print(redisClient.hkeys("Cloud_Accounts"))

print("The values present in the Redis hash:");

print(redisClient.hvals("Cloud_Accounts"))

print("The keys and values present in the Redis hash are:")

print(redisClient.hgetall("Cloud_Accounts"))