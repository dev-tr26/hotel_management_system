from django.contrib import admin
from .models import Payments, Supplier, Category, InventoryItem, Expense, PurchaseItem

@admin.register(Payments)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'booking', 'payment_mode', 'total_amount')
    list_filter = ('payment_mode',)
    search_fields = ('booking__booking_id',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'supplier_name', 'email', 'phone_number', 'contact_person')
    search_fields = ('supplier_name', 'email', 'phone_number')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
    search_fields = ('category_name',)


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_name', 'category', 'supplier', 'unit_price', 'quantity_in_stock')
    list_filter = ('category',)
    search_fields = ('item_name',)



@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_id', 'expense_date', 'category', 'amount', 'supplier', 'payment_method')
    list_filter = ('payment_method', 'category')
    search_fields = ('description',)

@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ('purchase_id', 'expense', 'item', 'quantity_purchased', 'unit_cost')
    search_fields = ('item__item_name',)