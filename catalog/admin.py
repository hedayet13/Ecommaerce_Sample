from django.contrib import admin
from .models import Category, Product, ProductImage, Variation, Attribute, AttributeValue, Review

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 0

@admin.register(Product)
class PAdmin(admin.ModelAdmin):
    list_display = ("name","category","price","is_active","created_at")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline, VariationInline]

@admin.register(Category)
class CAdmin(admin.ModelAdmin):
    list_display = ("name","parent","menu")
    prepopulated_fields = {"slug": ("name",)}

admin.site.register([Attribute, AttributeValue, Review])
