from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'guest', 'total_amount', 'order_datetime', 'room_no')
    search_fields = ('guest__first_name', 'guest__last_name')
    list_filter = ('order_datetime',)