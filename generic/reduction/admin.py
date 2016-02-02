from django.contrib import admin

# Register your models here.


from .models import Job, Reduction, Scan

admin.site.register(Job)
admin.site.register(Reduction)
admin.site.register(Scan)
