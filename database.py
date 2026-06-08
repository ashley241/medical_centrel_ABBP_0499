from pymongo import MongoClient

# 🔐 URL ACTUALIZADA: Con tu nueva contraseña sin caracteres especiales
MONGO_URI = "mongodb+srv://a24308051280499_db_user:PEREZ1234QWE@central1.h0bcnkb.mongodb.net/?appName=central1"

client = MongoClient(MONGO_URI)
db = client['Centralmedic']