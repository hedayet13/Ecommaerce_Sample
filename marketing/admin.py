from django.contrib import admin
from .models import Banner
@admin.register(Banner)
class BAdmin(admin.ModelAdmin):
    list_display = ("title","active","ordering")
    list_editable = ("active","ordering")
