from django.contrib import admin
from .models import Vendor
@admin.register(Vendor)
class VAdmin(admin.ModelAdmin):
    list_display = ("id","name","user")
