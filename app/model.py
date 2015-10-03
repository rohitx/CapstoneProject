"""
This function creates a model for the recommender system. The function takes
as input the user's choice of game and returns four games recommended by the
model.

File(s) used: None
Database(s) uses: MongoDB
                  Uses Collections:
                  PopularGames
                  IndieGames
Created: September 30th, 2015
Creator: Rohit Deshpande
"""

# Import Statements
from pymongo import MongoClient
import pandas as pd
from gensim import corpora, models, similarities
import operator
import getGameName

# Initialize Mongo Clients
client = MongoClient()
db_popGames = client.Games
cursor_popGames = db_popGames.PopularGames.find()
df_popGames = pd.DataFrame(list(cursor_popGames))

#print game_summary
# Get Indie Games Database
db_indieGames = client.Games
cursor_indieGames = db_indieGames.IndieGames.find()
df_indieGames = pd.DataFrame(list(cursor_indieGames))


def recommend_model(gameName):
    # Change the game to search for Metacritic MongoDB
    game_name = getGameName.clean_game_name(gameName)
    # Search for the game the user just selected:
    theGame = df_popGames[(df_popGames["game_name"] == game_name)]
    game_summary = theGame["summary"].iloc[0]
    #Get all summaries associated with IndieGames
    all_summaries = df_indieGames.summary

    #Load the model
    lsi_model = models.LsiModel.load('gensim_stuff/model_indie.lsi')

    # Load the corpus
    corpus = corpora.MmCorpus('gensim_stuff/IndieSummaries.mm')
    index = similarities.MatrixSimilarity(lsi_model[corpus])
    # Load the dictionary
    dictionary = corpora.Dictionary.load('gensim_stuff/IndieSummaries.dict')

    # Break the user input game into vector:
    vec_bow = dictionary.doc2bow(game_summary.lower().split())
    vec_lsi = lsi_model[vec_bow]

    sims = index[vec_lsi]

    sims_sorted = sorted(enumerate(sims), key=lambda item: -item[1])

    results = {}
    for val in sims_sorted[:4]:
        index, value = val[0], val[1]
        results[df_indieGames.game_name.loc[index]] = {
        # "Game Name": df_indieGames.game_name.loc[index],
        "Genre":df_indieGames.genre.loc[index],
        "Rating": df_indieGames.score.loc[index],
        "Link": df_indieGames.game_link[index],
        "Score": value
    }
    result = sorted(results.items(), key=operator.itemgetter(0), reverse=False)
    return result

if __name__ == '__main__':
    sim = recommend_model("007: NightFire")
    print sim

