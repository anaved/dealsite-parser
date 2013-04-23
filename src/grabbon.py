import urllib
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Naved"
__date__ ="$Jul 3, 2010 2:54:22 AM$"

from django.utils.encoding import smart_str, smart_unicode
import datetime
import re
from threading import Thread
import urllib2
from BeautifulSoup import BeautifulSoup

class grabbon(Thread):
   def __init__ (self,url):
      Thread.__init__(self)
      self.url = url
      self.status = -1
   def run(self):
    location=self.url
    u = urllib2.urlopen(location)
    data=u.read()
    data=unicode(data,errors='ignore')
    soup=BeautifulSoup(data)
#
    source=location
    source_name="Grabbon"
    city="Bangalore"
#
    
    name=soup.find('div', attrs={'class':'bannertext'}).string    

    deal=soup.find('div', attrs={'class':'dealdiv'})

    image_div=deal.find('div', attrs={'id':'middle'})
#
    image=image_div.find('img').get('src')


    dealportion=deal.find('div', attrs={'id':'dealportion'})
    dp= dealportion.findAll('div',attrs=({'class':'dealtext'}))
#       
    num_buyers=(dp[0].find(text=True) or dp[1].find(text=True)).split()[0]
    
#
    tipping_point= dp[1].findAll(text=True)[0].split()[0] or dp[2].findAll(text=True)[1].split()[-1]
    #tipping_point= dp[1].findAll(text=True)[1].split()[-1]
#
    cost_price=dealportion.find('div',attrs={'class':'value1'}).string.split('.')[-1]
#
    sell_price=dealportion.find('div',attrs={'class':'sale1'}).string.split('.')[-1]
#
    sell_price=float(cost_price)-float(sell_price)

    td= re.search('TargetDate.*',soup.findAll('script')[3].string)
    t=re.search('\".*\"',td.group(0)).group(0)
    end_time= datetime.datetime.strptime(t,"\"%m/%d/%Y %I:%M %p\"")
    cur_time=datetime.datetime.now()
    diff=end_time-cur_time
    minutes, seconds = divmod(diff.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    hours=hours+diff.days*24    
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
    print "printing grabbon"
    print pipe.read()
