import requests
import bs4
import redis
import cherrypy

root_url = 'https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G'
r = requests.get(root_url)
soup = bs4.BeautifulSoup(r.content)
fp=open('data.txt','w+')
fp.write( soup.select('div p')[0].get_text() + '\n')

fp.write( soup.select('div p')[4].get_text() + '\n\n')

for i in range(11, 21):
    table = (str(soup.select('tr a[href^=/live_market]')[i].get_text()))
table.append((str(soup.select('tr a[href^=/wiki]')[i].get_text())))

admission_date = (str(soup.select('tr span[style^="white"]')[i - 3].get_text()))

fp.write('%-15s  %-15s\n' % (a,b,c))


fp.write('\n\n')

fp.write( str(soup.select('ul li[id^="footer"]')[0].get_text() ).strip(' ') + '\n\n')

fp.close()
