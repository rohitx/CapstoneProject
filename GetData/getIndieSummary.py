from bs4 import BeautifulSoup
import urllib2, sys, random, time
import pandas as pd

df = pd.read_csv("IndieGamesToScrape.csv")
df.head()

gameLinks = df["link"].values

links = gameLinks[:10]

for site in links:
    #site = "http://www.indiedb.com/games/slender-a-new-darkness"
    page = urllib2.urlopen(site)
    soup = BeautifulSoup(page)

    mydivs = soup.find("div", {"class": "headernormalbox normalbox"})
    summary = mydivs.text
    mysummary =  summary[:2000].strip()
    print mysummary
    wait_time = random.randint(1,2)
    print "Waiting for...", wait_time
    time.sleep(wait_time)
    print "*"*80