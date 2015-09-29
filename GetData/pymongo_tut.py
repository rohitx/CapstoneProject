from pymongo import MongoClient
import pandas as pd

client = MongoClient()

# Pop Games
db_popGames = client.Games
cursor_popGames = db_popGames.PopularGames.find()
df_popGames = pd.DataFrame(list(cursor_popGames))

# Indie Games
db_indieGames = client.Games
cursor_indieGames = db_indieGames.IndieGames.find()
df_indieGames = pd.DataFrame(list(cursor_indieGames))
