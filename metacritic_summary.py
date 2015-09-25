from bs4 import BeautifulSoup
import urllib2, sys, time, random
import pandas as pd
import numpy as np

with open("PopGames.txt", "r") as g:
    content = g.readlines()

goFrom = 1420
goTo = goFrom + 10
content = content[goFrom:goTo]
print content

index = np.arange(goTo - goFrom)
columns = ["Game", "Summary"]
df = pd.DataFrame(columns = columns, index=index)

outfile = "metacritic/summaries"+str(goFrom)+"-"+str(goTo)+".json"
with open(outfile, "w") as z:
    for i, game in enumerate(content):
        org_game = game.strip()
        print game
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
        descp = descp.strip()
        wait_time = random.randint(3,5)
        print "Waiting for...", wait_time
        time.sleep(wait_time)
        print ""
        print ""
        df.ix[i,"Game"] = game
        df.ix[i,"Summary"] = descp
        #z.write("{ga:s} | {des:s}\n".format(ga=game, des=descp))
    z.close()
df.to_json(outfile)