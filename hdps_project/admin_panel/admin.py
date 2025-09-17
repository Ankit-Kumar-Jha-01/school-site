# admin.py
from django.contrib import admin
from .models import Student, Class, Subject, StudentFees, Months, GalleryImage

admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(StudentFees)
admin.site.register(Months)
admin.site.register(GalleryImage)
