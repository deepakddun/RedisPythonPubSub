import redis
import os
import subprocess
import sys

# os.system("python subscriber2.py")

print("Starting publisher")
test = redis.StrictRedis(host='redis-server', port=6379, db=0,decode_responses=True)

#subprocess.Popen(["nohup", "python", "./subscriber2.py"],env=os.environ)

test.publish("insert", "Hello World 1")

test.publish("insert", "Hello World 2")

test.publish("insert", "Hello World 3")

test.publish("insert", "Hello World 4")

print("The End")
