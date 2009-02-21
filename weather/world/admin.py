from django.contrib.gis import admin
from models import WorldBorders
from models import Resorts

admin.site.register(WorldBorders, admin.GeoModelAdmin)
admin.site.register(Resorts, admin.ModelAdmin)
