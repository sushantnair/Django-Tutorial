from django.contrib import admin

# Register your models here.

# PART A

'''
from .models import Courses

admin.site.register(Courses)
'''

# PART B

from .models import Courses
from .models import Person

admin.site.register(Courses)
admin.site.register(Person)
