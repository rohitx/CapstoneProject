with open('top100IndieGames.txt', 'r') as f:
    games = f.readlines()
f.close()

unique_games = list(set(games))
cleaned_games = [x.strip('\n') for x in unique_games]
cleaned_games.sort()
#print cleaned_games


with open('uniqueGames.txt', 'w') as f:
    for game in cleaned_games:
        f.write(game.encode('utf-8')+'\n')

f.close()