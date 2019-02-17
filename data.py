import grovepi
from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import csv
import  socket, struct, dweepy, time, platform
from random import randint

import sqlite3
from sqlite3 import Error
from subprocess import call
thingName  = []
thingRate = []



def post(dic):
    thing = 'jack'
    #print (dweepy.dweet_for(thing,dic))
#reading Sonic data from pi
def getSonic():
        sonic_ranger = 4
        Relay_pin = 2

        pinMode(Relay_pin,"OUTPUT")

        while True:
            try:
                distant = ultrasonicRead(sonic_ranger)
            except IOError:
                print("Error")
            return(distant)
#get tempeture and humidity
def gettemp():
	sensor = 3
	blue = 0
	white = 1
	while True:
            try:
                [temp,humidity] = grovepi.dht(sensor,blue)
                if math.isnan(temp) == False and math.isnan(humidity) == False:
                    print(".")
            except IOError:
                print ("Error")
            return(temp)
#just get humidity
def gethum():
	sensor = 3
	blue = 0
	white = 1
	while True:
            try:
                [temp,humidity] = grovepi.dht(sensor,blue)
                if math.isnan(temp) == False and math.isnan(humidity) == False:
                    print('..')
            except IOError:
                print ("Error")
            return(humidity)
#get light data
def getlight():
    light_sensor= 0
    while True:
        try:
            sensor_value = grovepi.analogRead(light_sensor)
            resistance = (float)(1023 - sensor_value) * 10 / sensor_value
        except IOError:
            print("erro")
        return(sensor_value)

def getReadings():
    dict = {}
    #putting all these into a dictornay so I can easily pop them out when something needs to be turned off
    dict["LightON"] = getlight()
    dict["SonicON"] = getSonic()
    dict["TempON"] = gettemp()
    dict["HumOn"] = gethum()
    return dict






def runn():
    while True:
        dict = getReadings()
        post(dict)
        time.sleep(5)

#checkAndroid()
