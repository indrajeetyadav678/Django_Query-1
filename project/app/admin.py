from django.contrib import admin
from .models import StudentModel

# Register your models here.
class Student(admin.ModelAdmin):
    list_display=['id','stu_address']
admin.site.register(StudentModel,Student)