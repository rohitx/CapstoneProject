from pymongo import MongoClient
from bs4 import BeautifulSoup
import urllib2, sys, random, time


def clean_game_name(game):
    """
    This function cleans the game of the game
    used to query Metacritic.com
    """
    if "&" in game:
            #game = game.replace(" ", "").replace("&", "-").lower()
        game = game.replace(" ","-").replace("&","").lower()
        game = game.replace(":", "")
        game = game.replace("'", "")
        game = game.replace("(", "").replace(")","").replace(" ", "-").lower()
    elif "(" in game:
        game = game.replace("(", "").replace(")","").replace(" ", "-").lower()
    else:
        game = game.replace(":", "")
        game = game.replace(",", "")
        game = game.replace("'", "")
        game = game.strip().replace(".", "")
        game = game.lower().replace(" ", "-")
    return game

def getScore(soup):
    """
    This function gets the Game Score
    for each game
    """
    score1 = soup.find_all("div", {"class":"metascore_w user large game mixed"})
    score2 = soup.find_all("div", {"class":"metascore_w user large game negative"})
    score3 = soup.find_all("div", {"class":"metascore_w user large game positive"})
    if len(score1) > 0:
        gameScore = score1[0].text
    elif len(score2) > 0:
        gameScore = score2[0].text
    elif len(score3) > 0:
        gameScore = score3[0].text
    else:
        gameScore = "NaN"
    return gameScore

def getGenre(soup):
    """
    This function gets the Genre
    of each game
    """
    genre = soup.find(itemprop="genre").text
    if len(genre) == 0:
        genre = "NaN"
    return genre

def getReview(soup):
    """
    This function gets the Review
    of each game.
    """
    review_count = soup.find(itemprop="reviewCount").text
    review_count = review_count.strip(" ")
    review_count = review_count.replace(" ", "")
    return review_count

def getSummary(soup):
    """
    This function gets the
    summary of each game
    """
    spans = soup.find('span',itemprop="description")
    if spans is not None:
        descp =  (spans.text).encode("utf-8")
    else:
        descp =  "None"
    descp = descp.strip()
    return descp


if __name__ == '__main__':
    # Initialize MongoDB
    client = MongoClient()
    db = client['Games']
    collection = db['PopularGames']
    # Read in the popular game names from file
    with open("PopGames.txt", "r") as g:
        content = g.readlines()

    content = content[1891:2000]

    for game in content:

        game = clean_game_name(game)

        site = "http://www.metacritic.com/game/pc/"+game
        print site
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(site,headers=hdr)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page)
        # Get the Score
        score = getScore(soup)

        # Get the Genre
        genre = getGenre(soup)

        # Get Review Count
        review_count = getReview(soup)

        # Get the Summary
        #descp = getSummary
        #print descp
        #
        spans = soup.find('span',itemprop="description")
        if spans is not None:
            descp =  (spans.text).encode("utf-8")
        else:
            descp =  "None"
        descp = descp.strip()
        #print descp

        # Insert values into the DataBase
        features = {
            '_id': game,
            'game_name': game,
            'game_link': site,
            'score': score,
            'genre': genre,
            'review_count': review_count,
            'summary': descp
        }
        collection.save(features)

        # Wait for the few seconds
        wait_time = random.randint(3,5)
        print "Waiting for...", wait_time
        time.sleep(wait_time)
        print ""
        print ""