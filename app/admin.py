from django.contrib import admin

# Register your models here.
from .models import Dog, DogOwner

admin.site.register(Dog)
admin.site.register(DogOwner)