from django.contrib.gis.db import models
from django.contrib.gis.measure import Distance

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

    def get_absolute_url(self):
        return "/resort/%s/" % self.pk

    def __unicode__(self):
        return self.name


class MeasuresResorts(models.Model):
    id = models.AutoField(primary_key=True)
    resort = models.ForeignKey(Resorts)
    altitude = models.IntegerField()

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

    class Meta:
        verbose_name_plural = "Measures"

    def __unicode__(self):
        return u"Measure taken at %s" % (self.taken_at)
