from django.contrib import admin
from .models import *
from shop.admin import BasketAdmin
from orders.admin import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    inlines = (BasketAdmin, OrderTabulareAdmin)
['Nothing', 'will', 'work', 'unless', 'you', 'do']
