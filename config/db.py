from pymongo import MongoClient
import urllib
username_raw = "############"
password_raw = "**************"
username_escaped = urllib.parse.quote_plus(username_raw)
password_escaped = urllib.parse.quote_plus(password_raw)
MONGO_URI = f"mongodb+srv://{username_escaped}:{password_escaped}@clusterpractice.3o5vagw.mongodb.net/"

conn = MongoClient(MONGO_URI)
print("Successfully connected to MongoDB!")