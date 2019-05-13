from django.db import models

# Create your models here.

class Dog(models.Model):
    owner_id = models.ForeignKey(DogOwner, on_delete=models.CASCADE)
    dog_name = models.CharField(max_length=100)

class DogOwner(models.Model):
    owner_name = models.CharField(max_length=100)
    owner_address = models.CharField(max_length=200)
    