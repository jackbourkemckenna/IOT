import urllib, json
import urllib2

from threading import Thread
from data import *
import requests
import time
class myClass(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
#running my runn method in thread 1 from the data.py file
        print ('Starting')
        runn()
class myClassSecond(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            test = ""
            dict1 = getReadings()

            #using pop to remove one of my sensors from the dictornay
            lst = dweepy.get_latest_dweet_for('Android')
            jsonL1 = lst[0]['content']['sensor']
            print jsonL1
            #values to check if on or off have been sent to dweet
            itemsOff = ["LightON","TempON","HumOn","SonicON"]
            if jsonL1 in itemsOff:
                #poppedDic = dict1
                test = str(jsonL1)
                print type(test)
                print test

                element = dict1.pop(test,None)


            time.sleep(5)
            print dict1


if __name__ == '__main__':
    a = myClass()
    b = myClassSecond()

    a.start()
    b.start()
