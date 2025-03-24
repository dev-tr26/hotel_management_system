from django.db import models
from employees.models import Employee


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_head_id = models.IntegerField()
    department_name = models.CharField(max_length=50)
    employee_underwork = models.IntegerField()

    class Meta:
        db_table = 'departments'

    def __str__(self):
        return self.department_name


class Room(models.Model):
    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
        ('Maintenance', 'Maintenance'),
    )
    
    room_id = models.AutoField(primary_key=True)
    room_type = models.CharField(max_length=50)
    room_no = models.CharField(max_length=20, unique=True)
    no_of_beds = models.IntegerField()
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='Available')

    class Meta:
        db_table = 'rooms'
        
    def __str__(self):
        return f"{self.room_no} ({self.room_type})"
    
    

class Service(models.Model):    
    service_id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True)
    
    class Meta:
        db_table = 'services'
        
    def __str__(self):
        return f'Service {self.service_id}'




  
class HousekeepingService(models.Model):
    STATUS_CHOICES = (
        ('Done', 'Done'),
        ('Working', 'Working'),
        ('Remaining', 'Remaining'),
    )

    housekeeping_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES)
    staff_assigned = models.ForeignKey('employees.Employee', on_delete=models.SET_NULL, null=True)
    service_date = models.DateField()

    class Meta:
        db_table = 'housekeeping_services'

    def __str__(self):
        return f"Housekeeping {self.housekeeping_id} - {self.room_no}"
    
    


class LuxurySpaService(models.Model):
    spa_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    treatment_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    service_date = models.DateField()

    class Meta:
        db_table = 'luxury_spa_services'

    def __str__(self):
        return f"Spa {self.treatment_type}"
    
    



class MultiCuisineRestaurantService(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    cuisine_type = models.CharField(max_length=50)
    seating_capacity = models.IntegerField()
    service_date = models.DateField()

    class Meta:
        db_table = 'multi_cuisine_restaurant_services'

    def __str__(self):
        return f"Restaurant {self.cuisine_type}"
    



class FitnessCenterService(models.Model):
    fitness_center_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    equipment_count = models.IntegerField()
    service_date = models.DateField()

    class Meta:
        db_table = 'fitness_center_services'

    def __str__(self):
        return f"Fitness Center {self.fitness_center_id}"
    



class TheaterService(models.Model):
    theater_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    seating_capacity = models.IntegerField()
    service_date = models.DateField()

    class Meta:
        db_table = 'theater_services'

    def __str__(self):
        return f"Theater {self.event_type}"
    


class FreeWifiService(models.Model):
    wifi_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    booking = models.ForeignKey('customers.Booking', on_delete=models.CASCADE)
    wifi_name = models.CharField(max_length=50)
    wifi_password = models.CharField(max_length=50)
    service_date = models.DateField()

    class Meta:
        db_table = 'free_wifi_services'

    def __str__(self):
        return f"Wifi {self.wifi_name}"
