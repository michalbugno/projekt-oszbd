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

    def get_absolute_url(self):
        return "/resort/%s/" % self.pk

    def __unicode__(self):
        return self.name

class Measures(models.Model):
    resort = models.ForeignKey(Resorts)
    temp = models.IntegerField()
    taken_at = models.DateField()

    class Meta:
        verbose_name_plural = "Measures"

    def __unicode__(self):
        return u"%s (%s)" % (self.resort.name, self.taken_at)
