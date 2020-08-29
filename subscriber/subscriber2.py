import redis

text_file = open("text_file","w")
text_file.write("INSIDE SUBSCRIBER\n")
client = redis.StrictRedis(host='redis-server', port=6379, db=0,decode_responses=True)

p = client.pubsub()

p.subscribe("insert")
#def event_handler(msg):
#    print(msg)


#p.subscribe(**{"insert": event_handler})

#p.run_in_thread(sleep_time=.001)

print("BEFORE while loop\n")
text_file.write("BEFORE FOR LOOP")
while True:
    message = p.get_message()
    if message:
        #print(message['data'])
        mes = str(message['data'])
        text_file.write(mes  + "\n")
        text_file.flush()

text_file.close()



