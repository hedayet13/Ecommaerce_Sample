from django.contrib import admin
from .models import Order, OrderItem, Address
class ItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
@admin.register(Order)
class OAdmin(admin.ModelAdmin):
    list_display = ("id","email","created_at","paid")
    inlines = [ItemInline]
admin.site.register(Address)
