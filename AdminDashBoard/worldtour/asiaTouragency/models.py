from django.db import models

# Create your models here
class Tour(models.Model):
    # we need to enter details of the trip
    origin_country=models.CharField(max_length=64)
    destination_country=models.CharField(max_length=64)
    number_of_nights=models.IntegerField()
    price=models.IntegerField()
    # this is a string representations
    def __str__(self) :
        return (f"Id: {self.id} From: {self.origin_country} To: {self.destination_country} Nights:{self.number_of_nights} Price:{self.price}")