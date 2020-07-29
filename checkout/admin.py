from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date', 'delivery_cost', 'order_total', 'grand_total')


admin.site.register(Order, OrderAdmin)

