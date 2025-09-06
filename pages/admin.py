from django.contrib import admin
from .models import Page
@admin.register(Page)
class PAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}
