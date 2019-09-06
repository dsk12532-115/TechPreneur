from django.contrib import admin

# Register your models here.
from .models import Profile, Vacant_Seats

admin.site.register(Profile)
admin.site.register(Vacant_Seats)