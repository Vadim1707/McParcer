from django.contrib import admin
from .models import McFoodInfo
# Register your models here.

@admin.register(McFoodInfo)
class McFoodInfoAdmin(admin.ModelAdmin):
    pass
