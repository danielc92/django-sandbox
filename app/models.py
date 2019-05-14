from django.db import models

# Models based on assumption that one dog can be owned by one owner
# and multiple dogs can be owned by one owner (one to many)

class DogOwner(models.Model):
    owner_name = models.CharField(max_length=100)
    owner_address = models.CharField(max_length=200)

    def __str__(self):
        return self.owner_name

class Dog(models.Model):
    owner_id = models.ForeignKey(DogOwner, on_delete=models.CASCADE)
    dog_name = models.CharField(max_length=100)
    dog_image = models.ImageField(upload_to='dogs/', default='dog_default.jpg')

    def __str__(self):
        return self.dog_name