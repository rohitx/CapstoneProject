import time
import random
from bs4 import BeautifulSoup
import urllib2

path = "/Users/rohit/git/CapstoneProject/IndieGameDB/"
for i in range(400,450):
    output_file = "page_"+str(i)+".txt"
    with open(path+output_file, "w") as f:
        r = urllib2.urlopen("http://www.indiedb.com/games/page/"+str(i)+"?filter=t&kw=&released=1&style=&theme=&indie=2&type=").read()
        soup = BeautifulSoup(r)
        mydivs = soup.findAll("div", { "class" : "row rowcontent clear" })
        for div in mydivs:
            link = div.find('a')['href']
            name = (link.split("/"))[-1]
            f.write("{l},{n}\n".format(l=link, n=name))
    f.close()
    wait_time = random.randint(1,10)
    print "Waiting for...", wait_time
    time.sleep(wait_time)