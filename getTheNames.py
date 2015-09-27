from bs4 import BeautifulSoup
import urllib2, sys, random, time


# Read in the popular game names from file
with open("PopGamesAlt.txt", "r") as g:
    content = g.readlines()
#g.close()

goFrom = 3312
goTo = 3606
a = content[goFrom:goTo]
outfile = "IndieDBGames/Links"+str(goFrom)+"-"+str(goTo)+".txt"
print "Doing...."
print a

with open(outfile, "w") as z:
    for game in a:
        print game
        gameurl = "http://indierecommender.net/output?game_select="+game
        d = urllib2.urlopen(gameurl).read()
        soup = BeautifulSoup(d)
        table = soup.find('table', 'table table-hover')
        links = table.findAll('a')
        for link in links:
            mylink = link['href']
            z.write("{ml:s}\n".format(ml=mylink))
        wait_time = random.randint(1,3)
        print "Waiting for...", wait_time
        time.sleep(wait_time)
z.close()