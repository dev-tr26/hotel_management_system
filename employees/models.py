from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField(null=True)
    email_id = models.CharField(max_length=100, unique=True, null=True)
    phone = models.CharField(max_length=15, null=True)
    department = models.ForeignKey('rooms.Department', on_delete=models.SET_NULL, null=True)
    designation = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'employees'

class Attendance(models.Model):
    STATUS_CHOICES = (
        ('P', 'Full Day Present'),
        ('H', 'Half Day Present'),
        ('A', 'Full Day Absence'),
    )

    attendance_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    attendance_status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        db_table = 'attendance'
        unique_together = ('employee', 'attendance_date')

class LeaveRequest(models.Model):
    LEAVE_TYPES = (
        ('Casual Leave', 'Casual Leave'),
        ('Medical Leave', 'Medical Leave'),
        ('Other', 'Other'),
    )
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    request_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=25, choices=LEAVE_TYPES)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Pending')

    class Meta:
        db_table = 'leave_requests'

    def __str__(self):
        return f"{self.employee} - {self.leave_type}"