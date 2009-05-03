from django.contrib.gis import admin
from models import *

admin.site.register(WorldBorders, admin.GeoModelAdmin)
admin.site.register(Resorts, admin.GeoModelAdmin)
admin.site.register(Measures, admin.ModelAdmin)
admin.site.register(MeasuresResorts, admin.ModelAdmin)
