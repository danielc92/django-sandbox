from django.db import models as m
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
    occupant_full_name = models.CharField(max_length=255)
    occupant_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.occupant_full_name

    class Meta:
        ordering = ('occupant_full_name',)

class Desk(m.Model):
    desk_no = models.CharField(default=uuid.uuid4)
    desk_level = models.IntegerField()
    desk_build_date = models.DateTimeField(auto_now_add = True)
    desk_info_modified = models.DateTimeField(auto_now = True)
    desk_weight = models.DecimalField()
    desk_cost = models.DecimalField()
    desk_width = models.DecimalField()
    desk_length = models.DecimalField()
    desk_occupant = models.ForeignKey(Occupant, on_delete=models.CASCADE)

    def __str__(self):
        return self.desk_no

    class Meta:
        ordering = ('desk_no',)
