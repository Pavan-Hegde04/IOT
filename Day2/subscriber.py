import json
import pymongo
import paho.mqtt.client as mqtt
#Instantiating an object with mqtt
client = mqtt.Client()

# Callback function - executed when the program successfully connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with flag "+str(flags)+"Connected with result code "+str(rc))
    client.subscribe("devices/#")

#Callback function - executed when the program gracefully disconnects from the broker
def on_disconnect(client, userdata, rc):
    print("Disconnected with result code "+str(rc))

#Callback function - executed whenever a message is published to the topics that 
#this program is subscribed to
def on_message(client, userdata, msg):
    item ={"topic":msg.topic,"payload":json.loads(msg.payload),"timestamp":json.loads(msg.payload)["timestamp"]}
    print(item)
    dbt.insert_one(item)
    print("Received a messsage on " + msg.topic + " and inserted it to the DB")

#Setting callback functions for various client actions
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

#Reading the configuration file
f=open("config_sub.json")
config=json.loads(f.read())
f.close()

#initialise mongo db
dbclient = pymongo.MongoClient(config["db_host"],config["db_port"])
db=dbclient[config["db_name"]]
dbt=db[config["db_collection"]]

#Connecting to broker
client.connect(host=config["broker_host"],port=config["broker_port"],keepalive=60)
client.username_pw_set(username="ccsession2", password="test")

'''
Start the MQTT client non-blocking loop to listen the broker for messages 
in subscribed topics and other operations for which the callback functions 
are defined
'''
client.loop_start()

while True:
    try:
        #Do nothing
        pass
    #Disconnect the client from MQTT broker and stop the loop gracefully at 
    # Keyboard interrupt (Ctrl+C)
    except KeyboarInterrupt():
        client.disconnect()
        client.loop_stop()
        break

