from pymongo import MongoClient
client = MongoClient()
db = client.Games
cursor = db.PopularGames.find()[:10]
