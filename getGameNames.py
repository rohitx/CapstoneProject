from bs4 import BeautifulSoup
import urllib2
import json
import pandas as pd

def getGameNames(full_url):
    output_file = ((full_url.split("/"))[-1]).split(".")[0]
    html_data3 = open(full_url, 'r').read()
    html_soup3 = BeautifulSoup(html_data3)
    response = []
    gameNames = html_soup3.findAll("div", { "class" : "tab_item_name" })
    gamelink = html_soup3.findAll("a", { "class" : ["tab_item", "tab_item_overlay", "a"]})
    tags = html_soup3.findAll("div", { "class" : ["tab_item_details", "platform_img", "top_tag" ]})
    data = {}

    for i in range(10,20):

        data["Value"] = i

        list =[]
        #***********
        # Game Name
        #***********
        data["Game"] = gameNames[i].text

        #**********
        # Game Link
        #**********
        data["Game Link"] = gamelink[i].get('href')

        #**********
        # Game Tags
        #**********
        if len(tags[i].text.strip("\n")) <= 1:
            data["GameTags"] =  None
        else:
            data["Game Tags"] = (tags[i].text).strip(" ")

        #*************
        # Game OS type
        #*************
        oslist = []
        list1 = [z for z in tags[i].children]
        for k in range(1,5):
            try:
                a = list1[k].attrs
                oslist.append(a['class'][1])
                data["OSType"] =  a['class'][1]
            except AttributeError:
                break
        data["OSType"] = oslist
        response.append(dict(data))

    a = json.dumps(response)
    df = pd.read_json(a)
    df.to_json("/Users/rohit/git/CapstoneProject/jsonFiles/"+output_file+'.json')
    return ""


# Read in the Steam Files
for i in xrange(1,276):
    if i < 10:
        full_url = "/Users/rohit/Desktop/SteamPowered/page0"+str(i)+".html"
    else:
        full_url = "/Users/rohit/Desktop/SteamPowered/page"+str(i)+".html"
    getGameNames(full_url)

# Concatenate json Files
result = []
for f in glob.glob("/Users/rohit/git/CapstoneProject/jsonFiles/*.json"):
    with open(f, "rb") as infile:
        result.append(json.load(infile))

with open("merged_file.json", "wb") as outfile:
     json.dump(result, outfile)

print "done with the job..."