from django.contrib import admin
from .models import Group, Event, Profile, Recipe, PhotoProfile, PhotoRecipe, PhotoEvent, PhotoGroup

# Register your models here.

admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Profile)
admin.site.register(Recipe)
admin.site.register(PhotoProfile)
admin.site.register(PhotoRecipe)
admin.site.register(PhotoEvent)
admin.site.register(PhotoGroup)

