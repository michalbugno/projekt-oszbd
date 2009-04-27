import os
import yaml

path = "./pydata/"

dirList = os.listdir(path)

for fname in dirList:

    f = open("./pydata/"+fname)

    data = yaml.load(f.read())

    for entry in data:
        print 
        print dirList[0].split('_')[2].capitalize()
        print dirList[0].split('_')[5].split('.')[0].upper()
        print
        print entry['date']
        print entry['time of day']
        print entry['clouds']
        print entry['wind']
        print entry['summary']
        print entry['snowfall']
        print entry['rainfall']
        print entry['max temp']
        print entry['min temp']
        print entry['wind chill']
        print entry['freeze'] 
