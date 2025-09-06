from django.contrib import admin
from .models import Post
@admin.register(Post)
class PAdmin(admin.ModelAdmin):
    list_display = ("title","created_at")
    prepopulated_fields = {"slug": ("title",)}
