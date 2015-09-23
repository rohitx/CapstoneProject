import pandas as pd
df = pd.read_csv("IndieGameCSV/page_1.csv", \
    names=["Windows","Mac","Linux","engine","release_date","year","genre1",\
           "theme","players","score_final","rating", "link" ], index_col=False)

# Remove the square brackets
for i in range(len(df.Windows)):
    df.Windows.loc[i] = df.Windows.loc[i].replace("[", "")

for i in range(len(df.Linux)):
    df.Linux.loc[i] = df.Linux.loc[i].replace("]", "")
print df.head()

new_df = df[df['link'].isnull()]
new_df['link'] = new_df['rating']
new_df['rating'] = new_df['score_final']
new_df['score_final'] = new_df['players']
new_df['players'] = new_df['theme']
new_df['theme'] = new_df['genre1']
new_df['genre1'] = new_df['year']
new_df['year'] = new_df['release_date'].apply(lambda x: x.split()[1])
new_df['release_date'] = new_df['release_date'].apply(lambda x: x.split()[0])
print new_df.head()

def clean_csv(filename):
    df = pd.read_csv(filename, \
    names=["Windows","Mac","Linux","engine","release_date","year","genre1",\
           "theme","players","score_final","rating", "link" ], index_col=False)
    # Remove the square brackets
    for i in range(len(df.Windows)):
        df.Windows.loc[i] = df.Windows.loc[i].replace("[", "")

    for i in range(len(df.Linux)):
        df.Linux.loc[i] = df.Linux.loc[i].replace("]", "")
