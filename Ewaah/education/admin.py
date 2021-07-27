from django.contrib import admin
from .models.college import College
from .models.collegeItem import CollegeItem


# Register your models here.

#donate
#school
#college
admin.site.register(College)
admin.site.register(CollegeItem)


