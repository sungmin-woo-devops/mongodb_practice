from pymongo import MongoClient

url = "mongodb://root:example@localhost:27017"
client = MongoClient()

try:
    client.admin.command('ping')
    print("Pinged yout deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
