from django.db import models
from django.core.exceptions import ValidationError

# Validator
def validate_number(value):
    if not value.isdigit():
        raise ValidationError('Invalid input. Please enter a number.')
# Booking model
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   phone_number = models.CharField(max_length=20, validators=[validate_number])
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name

#create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField()
   menu_item_description = models.TextField(max_length=1000, default='')

   def __str__(self):
       return self.name
