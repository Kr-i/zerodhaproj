
import bs4
import redis
import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "index.html"

url = 'http://delhi-ncr.yellowpages.co.in/Restaurant'

r = requests.get(url)

soup = bs4.BeautifulSoup(r.content)

print soup.prettify()

print soup.find_all("a")

links = soup.find_all("a")
try:
    for link in links:
        if "http" in link.get("href"):    
            print link.get("href"), link.text  

except:
    pass

data = soup.find_all("div", {"class": "live_market_content"})
listNames = []
listLoc = []
count = 1

for item in data:



        print(item.contents[1].find_all("h2", {"class": "tabs_main_content"})[0].text)  # prints name of restaurant
        print(item.contents[1].find_all("span")[0].text)
        print item.contents[3].find_all("h3",{"class":"tab_main_content"})[0].text

        print(item.contents[3].find_all("div", {"class": "tabContent")[0].text)



     print item.contents[0].find_all("h3",{"class":"tab8content"})[0].text)

    count += 1
}
