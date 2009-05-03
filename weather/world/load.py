import os
import yaml
from django.contrib.gis.utils import LayerMapping
from django.core.exceptions import ValidationError
from models import *

def load_fixtures():
  load_worldborders()
  load_resorts()
  load_measures()

def load_worldborders():
  WorldBorders.objects.all().delete()
  f = open("worldborders.fixtures")
  for i in range(0, 8):
    name = f.next().strip()
    poly = f.next().strip()
    coords = f.next().strip().split(" ")
    lon = float(coords[0])
    lat = float(coords[1])
    country = WorldBorders()
    country.name = name
    country.mpoly = poly
    country.lon = lon
    country.lat = lat
    country.save()
    print "Saved country '%s'" % country.name

def load_resorts():
  Resorts.objects.all().delete()
  f = open("resorts.fixtures")
  for line in f:
    resort_data = line.strip().split(" ")
    if len(resort_data) == 3:
      name = resort_data[0]
      lon = resort_data[1]
      lat = resort_data[2]
      resort = Resorts()
      resort.name = name
      resort.position = "POINT(%s %s)" % (lon, lat)
      resort.save()
      print "Saved resort '%s'" % resort.name

def load_measures():
  months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
  hours = {'morning': '08:00', 'afternoon': '16:00', 'night': '00:00'}
  abtenau = Resorts.objects.filter(name='Abtenau')[0]
  data_list = yaml.load(file.read(open('../pydata/abtenau.yml', 'r')))
  resorts = abtenau.measure_resorts()
  if len(resorts) == 0:
    measure_resort = MeasuresResorts()
    measure_resort.resort = abtenau
    measure_resort.altitude = 1500
    measure_resort.save()
  else:
    measure_resort = resorts[0]

  for data in data_list:
    measure_data = Measures()
    measure_data.measure_resort = measure_resort
    measure_data.max_temp = data['max temp']
    measure_data.min_temp = data['min temp']
    m, d = data['date'].split(' ')
    m = months[m]
    h = hours[data['time of day']]
    taken_at = "2008-%s-%s %s" % (str(m), str(d), str(h))
    measure_data.taken_at = taken_at
    try:
      measure_data.save()
    except:
      print "Couldn't save measure %s" % (taken_at)
    print "Saved measure %s" % (taken_at)
