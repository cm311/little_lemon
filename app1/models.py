from django.db import models

# Create your models here.
class DrinkCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Drink(models.Model):
    drink_name = models.CharField(max_length=200)
    prince = models.IntegerField()
    category_id = models.ForeignKey(DrinkCategory, on_delete=models.PROTECT, default=None)

class Employee(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    role = models.CharField(max_length = 100)
    shift = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name

class Booking(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)


class ShiftLogger(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    time_log = models.TimeField(help_text = "Enter the exact time!")





