from django.contrib import admin

from .models import *

admin.site.register(HealthGroup)
admin.site.register(SportGroup)
admin.site.register(SportClass)
admin.site.register(Attendance)
