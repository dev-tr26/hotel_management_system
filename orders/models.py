from django.db import models

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    guest = models.ForeignKey('customers.Guest', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_datetime = models.DateTimeField()
    room_no = models.ForeignKey('rooms.Room', on_delete=models.CASCADE, to_field='room_no')

    class Meta:
        db_table = 'orders'
    
    def __str__(self):
        return f"Order {self.order_id} - {self.guest}"