from django.db import models
from customers.models import Booking

class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length=50, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'payments'
        
    def __str__(self):
        return f"Payment {self.payment_id} - {self.total_amount}"
    

    
    
class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    address = models.TextField(null=True)
    contact_person = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Suppliers'

    def __str__(self):
        return self.supplier_name





class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'Categories'

    def __str__(self):
        return self.category_name




class InventoryItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=10)
    unit_of_measure = models.CharField(max_length=20, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Inventory_Items'

    def __str__(self):
        return self.item_name




class Expense(models.Model):
    PAYMENT_METHODS = (
        ('Cash', 'Cash'),
        ('Credit Card', 'Credit Card'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Check', 'Check'),
    )

    expense_id = models.AutoField(primary_key=True)
    expense_date = models.DateField()
    category = models.CharField(max_length=50)
    description = models.TextField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=25, choices=PAYMENT_METHODS, default='Cash')
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Expenses'

    def __str__(self):
        return f"Expense {self.expense_id} - {self.amount}"




class PurchaseItem(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity_purchased = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Purchase_Items'

    def __str__(self):
        return f"Purchase {self.purchase_id}"