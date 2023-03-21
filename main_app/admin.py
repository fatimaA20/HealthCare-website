from django.contrib import admin
from .models import Department ,Doctor , Patient , appointment,CustomUser
# Register your models here.

admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(CustomUser)
admin.site.register(appointment)