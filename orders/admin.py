from django.contrib import admin
from .models import *


class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "plant", "name", "price", "quantity"
    search_fields = (
        "plant",
        "name"
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "plant", "name", "price", "quantity"
    search_fields = (
        "order",
        "product",
        "name",
    )


class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "paymenr_on_get",
        "is_paid",
        "created_timestamp",
    )

    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "id",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    readonly_fields = ("created_timestamp",)
    list_filter = (
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    inlines = (OrderItemTabulareAdmin,)
['Nothing', 'will', 'work', 'unless', 'you', 'do']
