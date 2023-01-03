from django.contrib import admin
from . models import Links,packets_log,Links_log
# Register your models here.


admin.site.register(Links)
admin.site.register(Links_log)
admin.site.register(packets_log)