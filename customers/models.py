from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone 

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    check_in = models.DateField()
    check_out = models.DateField()
    booking_type = models.CharField(max_length=50, null=True)
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
    adults = models.IntegerField(default=0)
    children = models.IntegerField(default=0)

    class Meta:
        db_table = 'bookings'



class Guest(models.Model):
    TITLE_CHOICES = (
        ('Mr', 'Mr'),
        ('Ms', 'Ms'),
        ('Mrs', 'Mrs'),
        ('Dr', 'Dr'),
        ('Other', 'Other'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    guest_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    aadhar_no = models.CharField(max_length=12, unique=True, null=True)
    country_code = models.CharField(max_length=10, null=True)
    mobile_no = models.CharField(max_length=15, null=True)
    title = models.CharField(max_length=5, choices=TITLE_CHOICES, default='Mr')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    occupation = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    nationality = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=20, null=True)
    address = models.TextField(null=True)

    class Meta:
        db_table = 'guests'
        
    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name or ''}"
    



class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    feedback_date = models.DateField()
    comments = models.TextField(null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        db_table = 'feedback'

    def __str__(self):
        return f"Feedback {self.feedback_id} - Rating: {self.rating}"
    
    

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The email not found")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
    
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email