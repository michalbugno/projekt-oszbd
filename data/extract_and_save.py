import os
import yaml
import re

path = "pydata"

dirList = os.listdir(path)

for fname in dirList:
  f = open("./pydata/"+fname)
  is_yaml = re.compile("\.yml")
  if is_yaml.search(f.name):

    data = yaml.load(f.read())

    for entry in data:
        # print entry['clouds']
        # print entry['wind']
        # print entry['summary']
        # print entry['snowfall']
        # print entry['rainfall']
        # print entry['wind chill']
        # print entry['freeze'] 
        print entry['date']
        print entry['time of day']
        print entry['max temp']
        print entry['min temp']
