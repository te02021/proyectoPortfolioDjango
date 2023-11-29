from django.contrib import admin
from .models import Project, SaveContactMessage, Studies, Courses, Works, Skills

# Register your models here.

admin.site.register(Project)
admin.site.register(Studies)
admin.site.register(SaveContactMessage)
admin.site.register(Courses)
admin.site.register(Works)
admin.site.register(Skills)

