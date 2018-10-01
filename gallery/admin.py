from django.contrib import admin
from .models import *


# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)


admin.site.register(Editor)
admin.site.register(Image, ImageAdmin)
admin.site.register(category)
admin.site.register(Location)