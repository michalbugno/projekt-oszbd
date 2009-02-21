import os
from django.contrib.gis.utils import LayerMapping
from models import WorldBorders
from models import Resorts

world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/TM_WORLD_BORDERS-0.3.shp'))

def run(verbose=True):
    lm = LayerMapping(WorldBorders, world_shp, world_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)

def load_fixtures():
  load_worldborders()
  load_resorts()

def load_worldborders():
  WorldBorders.objects.all().delete()
  f = open("worldborders.fixtures")
  for i in range(0, 1):
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
