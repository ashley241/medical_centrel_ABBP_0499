from pymongo import MongoClient


MONGO_URI = "mongodb+srv://a24308051280499_db_user:Perez1234QWE@central1.h0bcnkb.mongodb.net/?appName=central1"

client = MongoClient(MONGO_URI)
db = client['Centralmedic']