import pymongo
import json

f=open("config_sub.json")
config=json.loads(f.read())
f.close()

#initialise mongo db
dbclient = pymongo.MongoClient(config["db_host"],config["db_port"])
db=dbclient[config["db_name"]]
dbt=db[config["db_collection"]]

#query documents
entries = dbt.find({"topic":"devices/temp","timestamp":{"$gte":"2021-09-21T19:52:46Z","$lt":"2021-09-22T19:53:06Z"}})
entries = dbt.find({"topic":"devices/hum","timestamp":{"$gte":"2021-09-21T19:52:46Z","$lt":"2021-09-22T19:53:06Z"}})



#Print the entries
for entry in entries:
    print(entry)

