from bs4 import BeautifulSoup
import urllib2, sys, random, time

# Read in the popular game names from file
with open("PopGames.txt", "r") as g:
    content = g.readlines()
#g.close()

goFrom = 600
goTo = goFrom + 50
a = content[goFrom:goTo]
outfile = "Info"+str(goFrom)+"-"+str(goTo)+".txt"
print "Doing...."
print a

# Create URLs to query MetaCritic.com
with open(outfile, "w") as z:
    for game in a:
        game = game.replace("&", "")
        game = game.replace("(", "")
        game = game.replace(")", "")
        game = game.replace(":", "")
        game = game.replace(",", "")
        game = game.replace("'", "")
        game = game.strip().replace(".", "")
        game = game.lower().replace(" ", "-")
        site = "http://www.metacritic.com/game/pc/"+game
        print site
        #site = "http://www.metacritic.com/game/pc/portal"
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(site,headers=hdr)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page)


        # Get the Summary
        spans = soup.find_all('span', {"class":"blurb blurb_expanded"})
        summary = []
        for span in spans:
            summary.append(span.string)
        if len(summary) == 0:
            summary = soup.find(itemprop="description").get_text()


        # Get the Score
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
            gameScore = "No Score"

        # Get the Genre
        genre = soup.find(itemprop="genre").text
        if len(genre) == 0:
            genre = "NaN"

        # Get Review Count
        #review_count = soup.find(itemprop="reviewCount").text
        #review_count = review_count.strip(" ")
        #review_count = review_count.replace(" ", "")

        # Write everything to file
        z.write("{sum:s} | {gs:s} | {ge:s} | {game:s} |\n".format(sum=summary, gs = gameScore, ge=genre, game=game))

        wait_time = random.randint(3,8)
        print "Waiting for...", wait_time
        time.sleep(wait_time)
z.close()