"""
This program takes in Indiedb.com links and scraps
Platform, engine, Release date, Genre, Theme, # of players,
summary, score, rating, and OS type into a MongoDB database.

File(s) used: IndieDBGamesLink.csv
Database(s) uses: MongoDB
                  Uses Collections:
                  IndieGames
Created: September 25th, 2015
Creator: Rohit Deshpande
"""


from bs4 import BeautifulSoup
import urllib2, sys, random, time
from pymongo import MongoClient
import pandas as pd

# Get Game Title
def getGameTitle(soup):
    title_div = soup.find("div", {"class":"title"})
    title = title_div.find("h2").text
    if len(title) == 0:
        return "NaN"
    else:
        return title

# Get Game Stats
def getGameStats(soup):
    soup = BeautifulSoup(z)
    mydivs = soup.findAll("div", { "class" : "row clear" })
    divlist = [a.text for a in mydivs]
    for l in divlist:
        a = l.split("\n")
        if 'Platform' in a or 'Platforms' in a:
            platform = a[2]
        if 'Engine' in a:
            engine =  a[2]
            engine = engine.encode('utf-8')
        if 'Release Date' in a:
            release_date = a[2]
            release_date = release_date.replace(",", "")
        if 'Genre' in a:
            genre = a[2]
        if 'Theme' in a:
            theme =  a[2]
        if 'Players' in a:
            players = a[2]
            players = players.replace(",", "")
    return platform, engine, genre, theme, players


# Get Score and Rating for each game
def getRatingScore(soup):
    divScore = soup.findAll("div", { "class" : "score" })
    divRating = soup.findAll("div", { "class" : "rating" })
    score = [s.text for s in divScore]
    rating = [r.text for r in divRating]
    if len(score) == 0:
        score_final = "NaN"
    else:
        s = score[0].replace('\n', '')
        score_final = s.split("Average")[-1]
    if len(rating) == 0:
        print "NaN"
    else:
        rating = (rating[0].strip("\n"))[:2]
    return score_final, rating

# Check the OS support for the game
# The choices are Windows, Mac, Linux
def checkOS(soup):
    ostype = {'Windows': False, 'Mac': False, 'Linux': False}
    oses = platform.split(",")
    oses = [x.strip() for x in oses]
    for p in oses:
        if p in ostype:
            ostype[p] = True
    platform_check = [value for key, value in ostype.iteritems()]
    return platform_check

if __name__ == '__main__':
     # Initialize MongoDB
    client = MongoClient()
    db = client['Games']
    collection = db['IndieGames']

    df = pd.read_csv("../IndieDBGamesLink.csv")
    mylinks = df['Links'].values

    fromlinks  = 1229

    mylinks = mylinks[fromlinks:]
    count = fromlinks
    for link in mylinks:
        print count
        print link
        print ""
        print ""
        z = urllib2.urlopen(link).read()
        soup_game = BeautifulSoup(z)

        # Get Game name as ID
        game_id = link.split("/")[-1]

        # Get Game Title
        game_title = getGameTitle(soup_game)

        # Get the Stats
        platform, engine, genre, theme, players = getGameStats(soup_game)

        # Get the Score, Rating
        score_final, rating = getRatingScore(soup_game)

        # Get the OStype
        ostype = checkOS(soup_game)


        divSummary = soup_game.findAll("div", { "class" : "headernormalbox normalbox" })
        summary = [s.text for s in divSummary]
        if len(summary) != 0:
            sum_short = summary[:2000]

        # Insert values into the DataBase
        features = {
                '_id': game_id,
                'game_name': game_title,
                'game_link': link,
                'Windows': ostype[0],
                'Mac': ostype[1],
                'Linux': ostype[2],
                'engine': engine,
                'genre': genre,
                'theme': theme,
                'players':players,
                'score': score_final,
                'review_count': rating,
                'summary': summary,
                'summary_short': sum_short
        }
        collection.save(features)
        count += 1

        #print game_id, game_title, ostype, engine, genre, theme, players
        #print score_final, rating
        #sum_short

        wait_time = random.randint(1,3)
        print "Waiting for...", wait_time
        time.sleep(wait_time)

