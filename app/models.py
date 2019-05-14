from django.db import models as m

# Models based on assumption that one dog can be owned by one owner
# and multiple dogs can be owned by one owner (one to many)

class DogOwner(m.Model):
    owner_name = m.CharField(max_length=100)
    owner_address = m.CharField(max_length=200)

    def __str__(self):
        return self.owner_name

class Dog(m.Model):
    owner_id = m.ForeignKey(DogOwner, on_delete=m.CASCADE)
    dog_name = m.CharField(max_length=100)
    dog_image = m.ImageField(upload_to='dogs/%Y/%m/%d/', 
                                 default='default.jpg')

    def __str__(self):
        return self.dog_name