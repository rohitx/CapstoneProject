from bs4 import BeautifulSoup
import urllib2, glob, random, time
import pandas as pd

def getIndieGameInfo(gameurl):
    d = urllib2.urlopen(gameurl).read()
    soup = BeautifulSoup(d)

    mydivs = soup.findAll("div", { "class" : "row clear" })

    #mydivs.findAll('a', 'href'=True)


    mylist = []
    for a in mydivs:
        mylist.append(a.text)

    for l in mylist:
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


    divScore = soup.findAll("div", { "class" : "score" })
    divRating = soup.findAll("div", { "class" : "rating" })
    score = []
    rating = []
    for s in divScore:
        score.append(s.text)
    for r in divRating:
        rating.append(r.text)

    s = score[0].replace('\n', '')
    score_final = s.split("Average")[-1]
    rating = (rating[0].strip("\n"))[:3]

    # Break platform into Boolean
    ostype = {'Windows': False, 'Mac': False, 'Linux': False}
    oses = platform.split(",")
    oses = [x.strip() for x in oses]
    for p in oses:
        if p in ostype:
            ostype[p] = True
    #print ostype
    platform_check = [value for key, value in ostype.iteritems()]

    return platform_check, engine, release_date,\
           genre, theme, players, score_final, rating


pages = glob.glob("/Users/rohit/git/CapstoneProject/IndieGameDB/*.txt")
if len(pages) == 0:
    print "No files found!"
pages = pages[300:444]
print pages
for page in pages:
    print "Doing page number...", page
    outfile = (page.split("/")[-1]).split(".")[0]+".csv"
    with open(outfile, "w") as f:
        df = pd.read_csv(page, sep=",", names = ["link", "game"])
        try_games = df.link
        for game in try_games:
            gameurl = "http://indiedb.com"+game
            print "Doing game...", gameurl
            platform_check, engine, release_date, genre, theme, players, score_final, rating = getIndieGameInfo(gameurl)
            f.write("{p:s},{e:s},{r:s},{g:s},{t:s},{pl:s},\
                     {sf:s},{ra:s}, {grl:s}\n".format(p=platform_check, e=engine, r=release_date,\
                                            g=genre, t=theme, pl=players, sf=score_final, ra=rating, grl=gameurl))
            wait_time = random.randint(1,2)
            print "Waiting for...", wait_time
            time.sleep(wait_time)
    f.close()
    print "Done with page...", outfile
    print "*"*80


print "Done writing the file..."
