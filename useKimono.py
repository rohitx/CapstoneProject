import json
import urllib
import random, time

# Read in the popular game names from file
with open("PopGames.txt", "r") as g:
    content = g.readlines()

goFrom = 1053
goTo = goFrom + 10
a = content[goFrom:goTo]
outfile = "metacritic/kimono"+str(goFrom)+"-"+str(goTo)+".txt"
print "Doing...."
print a
website = "https://www.kimonolabs.com/api/ondemand/51vmw31a?"
apikey = "2U4MBbqqb42XVuB5fmxrbYWuOwsiWKDA"

# Create URLs to query MetaCritic.com
with open(outfile, "w") as z:
    for game in a:
        print "Doing...", game
        game = game.replace("&", "")
        game = game.replace("(", "")
        game = game.replace(")", "")
        game = game.replace(":", "")
        game = game.replace(",", "")
        game = game.replace("'", "")
        game = game.strip().replace(".", "")
        game = game.lower().replace(" ", "-")
        results = json.load(urllib.urlopen(website+apikey+"&kimpath3="+game))
        values = []
        for a in results['results']['collection1']:
            values.append(a['property1']['text'].encode('utf-8'))
        release_date = (values[2]).replace(",","")
        genre = values[8]
        summary = values[4]
        z.write("{su:s}|{re:s}|{ge:s}|{ga:s}\n".format(su=summary, re=release_date, ge=genre, ga=game))
        wait_time = random.randint(3,8)
        print "Waiting for...", wait_time
        time.sleep(wait_time)
    z.close()


#results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/dscd2pp2?apikey=2U4MBbqqb42XVuB5fmxrbYWuOwsiWKDA"))



#results = json.load(urllib.urlopen(website+apikey+"&kimpath3="+game)
#results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/ondemand/51vmw31a?apikey=2U4MBbqqb42XVuB5fmxrbYWuOwsiWKDA&kimpath3=banished"))


#values = []
#for a in results['results']['collection1']:
#    values.append(a['property1']['text'].encode('utf-8'))