from bs4 import BeautifulSoup as soup
from pymongo import MongoClient
import pymongo
import certifi


def get_database():    
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://alddsdataanalytics:ALDDSgoogle.2022@alddsdataanalytics.gjtom.mongodb.net/alddsdataanalytics"
    
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    
    client = pymongo.MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
    print("Connected successfully!!!")

    return client['alddsdataanalytics']


def query_from_db():
    dbname = get_database()
    collection = dbname["alddsdataanalytics"]
    #Get the latest record
    item_details = collection.find().sort("time", -1)
    data = item_details[0]
    return  data

