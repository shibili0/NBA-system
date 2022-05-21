from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Course_Outcome)
admin.site.register(Program_Outcome)
admin.site.register(Program_Specific_Outcome)