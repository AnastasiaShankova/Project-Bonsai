from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)


class PlantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "image", "available_quantity")
    search_fields = ('name', 'category')
    list_filter = ('name', 'category')
    list_display_links = ('id', 'name', 'category')
    ordering = ('category',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('plant', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0


admin.site.register(Category, CategoryAdmin)
admin.site.register(Plant, PlantAdmin)
admin.site.register(Basket)
['Nothing', 'will', 'work', 'unless', 'you', 'do']
