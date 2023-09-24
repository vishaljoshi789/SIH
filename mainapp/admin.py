from django.contrib import admin
from .models import SchoolData, CollegeData, School, College
# Register your models here.

admin.site.register(SchoolData)
admin.site.register(CollegeData)
admin.site.register(School)
admin.site.register(College)
