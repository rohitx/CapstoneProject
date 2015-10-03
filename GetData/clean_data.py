import pandas as pd
import numpy as np
df = pd.read_csv("/Users/rohit/Desktop/IndieGames_CSV/allGames.csv", \
    names=["Windows","Mac","Linux","engine","release_date","genre",\
           "theme","players","score_final","rating", "link" ])

#Remove the square brackets
df["Windows"] = df["Windows"].apply(lambda x: x.replace("[", ""))
df["Linux"] = df["Linux"].apply(lambda x: x.replace("]", ""))
df["score_final"] = df["score_final"].apply(lambda x: x.strip())
# Set score_final to float
df['score_final'] = df['score_final'].apply(lambda x: np.nan if x=='-' else float(x))
df_games = df[(df["Windows"] == 'True') | (df['Mac'] == 'True') | (df['Linux'] == 'True')]

# All new games
df_final = df_game.dropna()

# Remove the brackets
def clean_csv(filename):
    df = pd.read_csv(filename, \
    names=["Windows","Mac","Linux","engine","release_date","year","genre1",\
           "theme","players","score_final","rating", "link" ], index_col=False)

    # Remove the square brackets
    for i in range(len(df.Windows)):
        df.Windows.loc[i] = df.Windows.loc[i].replace("[", "")

    for i in range(len(df.Linux)):
        df.Linux.loc[i] = df.Linux.loc[i].replace("]", "")

    # Create a new dataframe where Either windows, mac, or Linux is true
    df_games = df[(df["Windows"] == 'True') | (df['Mac'] == 'True') | (df['Linux'] == 'True')]
    return None
