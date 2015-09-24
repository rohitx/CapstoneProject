from bs4 import BeautifulSoup
import urllib2, sys, time, random


with open("PopGames.txt", "r") as g:
    content = g.readlines()

goFrom = 600
goTo = 800
content = content[goFrom:goTo]
print content

outfile = "metacritic/summaries"+str(goFrom)+"-"+str(goTo)+".txt"
with open(outfile, "w") as z:
    for game in content:
        org_game = game
        print game
        if "&" in game:
            #game = game.replace(" ", "").replace("&", "-").lower()
            game = game.replace(" ","-").replace("&","").lower()
            game = game.replace(":", "")
            game = game.replace("'", "")
        elif "(" in game:
            game = game.replace("(", "").replace(")","").replace(" ", "-").lower()
        else:
            game = game.replace(":", "")
            game = game.replace(",", "")
            game = game.replace("'", "")
            game = game.strip().replace(".", "")
            game = game.lower().replace(" ", "-")
        site = "http://www.metacritic.com/game/pc/"+game
        print site
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(site,headers=hdr)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page)
        spans = soup.find('span',itemprop="description")
        if spans is not None:
            descp =  (spans.text).encode("utf-8")
        else:
            descp =  "None"
        wait_time = random.randint(3,8)
        print "Waiting for...", wait_time
        time.sleep(wait_time)
        print ""
        print ""
        z.write("{ga:s} | {gr:s} | {des:s}\n".format(ga=game, gr=org_game, des=descp))
        print goFrom + content.index(org_game)

    z.close()