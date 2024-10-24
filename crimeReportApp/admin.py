from django.contrib import admin

# Register your models here.

from .models import CrimeReports

admin.site.register(CrimeReports)
