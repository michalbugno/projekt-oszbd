from django.contrib.gis import admin
from models import WorldBorders
from models import Resorts
from models import Measures

admin.site.register(WorldBorders, admin.GeoModelAdmin)
admin.site.register(Resorts, admin.GeoModelAdmin)
admin.site.register(Measures, admin.ModelAdmin)
