from django.contrib.gis.db import models
from django.contrib.gis.measure import Distance
from world.drawer import Drawer
from django import db

class WorldBorders(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    lat = models.FloatField()
    lon = models.FloatField()
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = "World Borders"

    def __unicode__(self):
        return self.name

class Resorts(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    position = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = "Resorts"

    def within_distance(self, distance):
        d = Distance(km=distance)
        return Resorts.objects.filter(position__dwithin=(self.position, d)).exclude(pk=self.pk)

    def country(self):
        countries = WorldBorders.objects.filter(mpoly__contains=self.position.wkt)
        if len(countries) > 0:
            return countries[0]
        else:
            return None

    def measure_resorts(self):
        return MeasuresResorts.objects.filter(resort__name=self.name)


    def draw_isoterms(self, date, temps, buffer_width, distance, filename):
        a = WorldBorders.objects.filter(name='Austria')[0]
        d = Drawer(a.mpoly.coords[0][0])
        for temp in temps:
          d.draw_poly(self.similar_coords(date, temp, buffer_width, distance))
        d.save(filename)


    def similar_coords(self, date, temperature, buffer_width, distance):
        distance_km = Distance(km=distance)
        date = date.date()
        points = None
        points_data = Resorts.objects.filter(position__dwithin=(self.position, distance_km), measuresresorts__measures__min_temp__lt=temperature, measuresresorts__measures__taken_at=date).unionagg()
        #points_data = Resorts.objects.filter(position__dwithin=(self.position, distance_km), measuresresorts__measures__min_temp__lt=temperature).unionagg()

        points = points_data.coords
        points_string = str(points + points[0]).replace("(", "").replace(")", "")

        cursor = db.connection.cursor()
        # sql = "SELECT SDO_UTIL.TO_WKTGEOMETRY(SDO_GEOM.SDO_BUFFER(MDSYS.SDO_GEOMETRY(2003, 4326, NULL, SDO_ELEM_INFO_ARRAY(1, 2003, 1), SDO_ORDINATE_ARRAY(%s)), 5000, 50, 'unit=m')) FROM WORLD_WORLDBORDERS;" % (points_string)
        sql = "SELECT SDO_UTIL.TO_WKTGEOMETRY(SDO_GEOM.SDO_BUFFER(SDO_GEOM.SDO_BUFFER(SDO_GEOM.SDO_CONVEXHULL(MDSYS.SDO_GEOMETRY(2003, 4326, NULL, SDO_ELEM_INFO_ARRAY(1, 2003, 1), SDO_ORDINATE_ARRAY(%s)), 50), %d, 50, 'unit=m'), %d, 50, 'unit=m')) FROM WORLD_WORLDBORDERS;" % (points_string, - buffer_width * 1000, (buffer_width) * 1000)
        print sql
        cursor.execute(sql)
        output = cursor.fetchone()[0]

        poly_coords = []
        for coords in str(output)[8:].replace("(", "").replace(")", "").split(", "):
            poly_coords.append(map(float, coords.split(" ")))
        return poly_coords


    def get_absolute_url(self):
        return "/resort/%s/" % self.pk

    def __unicode__(self):
        return self.name


class MeasuresResorts(models.Model):
    id = models.AutoField(primary_key=True)
    resort = models.ForeignKey(Resorts)
    altitude = models.IntegerField()
    objects = models.GeoManager()

    def measures(self):
        return Measures.objects.filter(measure_resort=self)

    class Meta:
        verbose_name_plural = "MeasuresResorts"

    def __unicode__(self):
        return u"%s at %dm" % (self.resort, self.altitude)


class Measures(models.Model):
    id = models.AutoField(primary_key=True)
    measure_resort = models.ForeignKey(MeasuresResorts)
    taken_at = models.DateTimeField()
    # freezing_level = models.IntegerField()
    # clouds = models.CharField(max_length=20)
    # wind = models.CharField(max_length=5)
    # summary = models.CharField(max_length=20)
    # snowfall = models.IntegerField()
    # rainfall = models.IntegerField()
    max_temp = models.IntegerField()
    min_temp = models.IntegerField()
    # wind_chill = models.IntegerField()
    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = "Measures"

    def __unicode__(self):
        return u"Measure taken at %s" % (self.taken_at)
