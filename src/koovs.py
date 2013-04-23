import BeautifulSoup
import re
from threading import Thread
import urllib
import urllib2


__author__="naved"
__date__ ="$3 Jul, 2010 6:46:16 PM$"

class koovs(Thread):
   def __init__ (self,url,city):
      Thread.__init__(self)
      self.url = url
      self.city=city
      self.status = -1
   def run(self):
    source=self.url
    u = urllib2.urlopen(source)
    data=u.read()
    bs=BeautifulSoup(data)
#    
    source_name="Koovs"
    city=self.city

    d=bs.find('div', attrs={'class':'deals'})
    ds = d.findAll('div', attrs={'class':re.compile('deal')}, recursive=False)
    for i in [0,1]:
        d1=ds[i]
        image = self.url + d1.findAll('img')[0].get('src')
        desc = d1.find('a', attrs={'class':'dealheading'})
        source_url = self.url + desc.get('href')
        name=desc.string[desc.string.index('worth of')+9:].title()
        prices = d1.findAll('div', attrs={'class':re.compile('prec')})
        cost_price = prices[0].find('b', attrs={'class':'bigfont'}).string
        sell_price = prices[2].find('b', attrs={'class':'bigfont'}).string
        numbers = d1.find('div', attrs={'class':re.compile('deal-numbers')})
        num_buyers = numbers.find('span', attrs={'class':'deal_bought'}).string
        tipping_point=re.search('Tipped when (\d+) bought',numbers.find(text=re.compile('Tipped when .*? bought'))).groups()[0]
        hours = d1.find('b', attrs={'class':'hour'}).string
        minutes = d1.find('b', attrs={'class':'min'}).string
        secs = d1.find('b', attrs={'class':'sec'}).string
        data={"source":source,
                "source_name":source_name,
                "city":city,
                "name":name,
                "image":image,
               "num_buyers":num_buyers,
               "tipping_point":tipping_point,
               "cost_price":cost_price,
               "sell_price":sell_price,
               "hours":hours,
               "minutes":minutes
        }
        data=urllib.urlencode(data)
        pipe= urllib2.urlopen('http://www.groupalong.com/api/add_product/?'+data)
        print "printing koovs"
        print pipe.read()

