import numpy as np
import graphlab
import pandas as pd
import cPickle as pickle

df = pd.read_table('data/u.data',
                   names=["user", "movie", "rating", "timestamp"])
sf = graphlab.SFrame(df[['user', 'movie', 'rating']])

rec = graphlab.recommender.factorization_recommender.create(
            sf,
            user_id='user',
            item_id='movie',
            target='rating',
            solver='als',
            side_data_factorization=False)

with open('data/recommender.pkl', 'w') as f:
    pickle.dump(rec, f)