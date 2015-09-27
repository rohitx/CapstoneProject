from bs4 import BeautifulSoup
import urllib2
import glob


files = glob.glob("/Users/rohit/Desktop/SteamPowered/page01.html")
with open("gameFile_test.txt", "w") as f:
    for full_url in files:

        html_data3 = open(full_url, 'r').read()
        html_soup3 = BeautifulSoup(html_data3)
        response = []
        gameNames = html_soup3.findAll("div", { "class" : "tab_item_name" })
        gamelink = html_soup3.findAll("a", { "class" : ["tab_item", "tab_item_overlay", "a"]})
        tags = html_soup3.findAll("div", { "class" : ["tab_item_details", "platform_img", "top_tag" ]})

        for i in range(10,20):

            list =[]
            #***********
            # Game Name
            #***********
            f.write(gameNames[i].text)

            #**********
            # Game Link
            #**********
            f.write(gamelink[i].get('href'))

            #**********
            # Game Tags
            #**********
            if len(tags[i].text.strip("\n")) <= 1:
                f.write(None)
            else:
                f.write((tags[i].text).strip(" "))

            #*************
            # Game OS type
            #*************
            oslist = []
            list1 = [z for z in tags[i].children]
            for k in range(1,5):
                try:
                    a = list1[k].attrs
                    oslist.append(a['class'][1])
                    #data["OSType"] =  a['class'][1]
                except AttributeError:
                    break

            #f.write(oslist)
f.close()