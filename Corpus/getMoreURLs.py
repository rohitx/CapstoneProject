import pandas as pd
import webbrowser
from bs4 import BeautifulSoup
import urllib2, sys, random, time

df = pd.read_csv("../IndieGamesToScrape.csv")
df_min = df["link"][:3]
for i, link in enumerate(df_min):
    url = link.strip()
    z = urllib2.urlopen(link).read()
    soup_game = BeautifulSoup(z)
    divSummary = soup_game.findAll("div", { "class" : "headernormalbox normalbox" })
    summary = [s.text for s in divSummary]
    u_summary = summary[0].encode("utf-8")
    print "Length of Summary: ", len(u_summary)
    if len(u_summary) > 200:
        sum_short = summary[:2000]
        print sum_short
    wait_time = random.randint(1,2)
    print "Waiting for...", wait_time
    time.sleep(wait_time)

    #webbrowser.open(url, new=0)
    #raw_input("Enter to continue...")

print "Done with all..."