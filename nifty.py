import redis
import cherrypy
import requests


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
r.get('foo')
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)


my_url = 'https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_BeautifulSoup = BeautifulSoup(page_html, "html.parser")
print(page_BeautifulSoup.h1)
Dates = str(soup.select('div#sidebar dd')[4].get_text()).strip('\n')

fp.write('%-70s  %-30s  %-80s %-20s\n' % (a,b,c,d))


