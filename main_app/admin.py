from django.contrib import admin
from .models import Group, Event, Profile, Recipe

# Register your models here.

admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Profile)
admin.site.register(Recipe)

