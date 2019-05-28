from django.db import models as m
from django.urls import reverse
from datetime import datetime
from tinymce.models import HTMLField
import uuid
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
    dog_image = m.ImageField(upload_to='dogs/%Y/%m/%d/', default='default.jpg')

    def __str__(self):
        return self.dog_name


class Tag(m.Model):
    tag_name = m.CharField(max_length=50)

    def __str__(self):
        return self.tag_name


class Article(m.Model):
    article_name = m.CharField(max_length=100)
    article_content = HTMLField()
    article_ct_date = m.DateTimeField(default=datetime.now)

    tags = m.ManyToManyField(Tag)

    def __str__(self):
        return self.article_name



class Occupant(m.Model):
    occupant_full_name = m.CharField(max_length=255)
    occupant_joined = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.occupant_full_name

    class Meta:
        ordering = ('occupant_full_name',)


class Desk(m.Model):
    desk_no = m.CharField(default=uuid.uuid4, max_length=255)
    desk_level = m.IntegerField()
    desk_build_date = m.DateTimeField(auto_now_add = True)
    desk_info_modified = m.DateTimeField(auto_now = True)
    desk_weight = m.DecimalField(max_digits=10, decimal_places=2)
    desk_cost = m.DecimalField(max_digits=10, decimal_places=2)
    desk_width = m.DecimalField(max_digits=10, decimal_places=2)
    desk_length = m.DecimalField(max_digits=10, decimal_places=2)
    desk_occupant = m.ForeignKey(Occupant, on_delete=m.CASCADE)

    def __str__(self):
        return self.desk_no

    def return_fields(self):
        return ['desk_no', 'desk_level', 'desk_build_date', 'desk_info_modified', 
        'desk_weight', 'desk_width', 'desk_length', 'desk_occupant']
    
    def get_absolute_url(self):
        return reverse('desk_list_view')

    class Meta:
        ordering = ('desk_no',)

