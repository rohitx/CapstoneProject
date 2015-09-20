"""
This program gets the names of top 100 Indie games
from the Indiedb website. The function takes in a URL
and returns a text file with the name of the games

Created: Sept. 19th 2015
Creator: Rohit Deshpande
"""



from bs4 import BeautifulSoup
import urllib2


def getText(url, outputFile):
    r = urllib2.urlopen(url).read()
    soup = BeautifulSoup(r)
    games = soup.find_all('h4')
    with open(outputFile, 'w') as f:
        for game in games:
            f.write(game.text.encode('utf8')+"\n")
    f.close
    return None

file = "http://www.indiedb.com/groups/2014-indie-of-the-year-awards/top100"
getText(file, "Indie2014.txt")
