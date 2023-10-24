from django.db import models
from datetime import datetime
from users.models import CustomUser
# Create your models here.

start_choice = (
    ("15:00", "15:00"),
    ("15:30", "15:30"),
    ("16:00", "16:00"),
    ("16:30", "16:30"),
    ("17:00", "17:00"),
    ("17:30", "17:30"),
)

end_choice = (
    ("15:30", "15:30"),
    ("16:00", "16:00"),
    ("16:30", "16:30"),
    ("17:00", "17:00"),
    ("17:30", "17:30"),
    ("18:00", "18:00"),
)

class UsersCustomuser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    full_name = models.CharField(max_length=25, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_customuser'

class Reservation(models.Model):
    user = models.ForeignKey(UsersCustomuser, models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(default=datetime.now)
    time_start = models.CharField(max_length=6,choices=start_choice)
    time_end = models.CharField(max_length=6,choices=end_choice, null=True)
    time_reservation = models.DateTimeField(default=datetime.now, blank=True)
    price = models.FloatField(null=True)

class PriceList(models.Model):
    time = models.CharField(max_length=10)
    price = models.FloatField()