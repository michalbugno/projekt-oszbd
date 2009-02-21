from django.contrib.gis.db import models
from django.contrib.gis.measure import Distance

class WorldBorders(models.Model):
    name = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = "World Borders"

    def __unicode__(self):
        return self.name

class Resorts(models.Model):
    name = models.CharField(max_length=50)
    # latitude = models.FloatField()
    # longitude = models.FloatField()
    position = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = "Resorts"

    def within_distance(self, distance):
      d = Distance(km=distance)
      return Resorts.objects.filter(position__dwithin=(self.position, d)).exclude(pk=self.pk)

    def get_absolute_url(self):
      return "/resort/%i/" % self.id

    def __unicode__(self):
      return self.name
