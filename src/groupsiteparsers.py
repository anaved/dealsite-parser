# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "naved"
__date__ = "$2 Jul, 2010 5:36:45 PM$"

from time import sleep

import grabbon
import taggle

if __name__ == "__main__":
  while(True):
    parsers = []

    grab_main = grabbon.grabbon('http://www.grabbon.com')
    parsers.append(grab_main)
    grab_main.start()


    grab_side = grabbon.grabbon('http://www.grabbon.com/channel/side')
    parsers.append(grab_side)
    grab_side.start()


    grab_side = grabbon.grabbon('http://www.grabbon.com/channel/offbeat')
    parsers.append(grab_side)
    grab_side.start()

#
#
    tag = taggle.taggle('http://www.taggle.com')
    parsers.append(tag)
    tag.start()

    sleep(3600)
#



#    report = ("No response", "Partial Response", "Alive")
#    for parser in parsers:
#        parser.join()
#        print "Status from ", parser.url, "is", report[parser.status]





    