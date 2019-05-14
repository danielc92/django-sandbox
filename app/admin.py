from django.contrib import admin

# Register your models here.
from .models import Dog, DogOwner, Tag, Article

admin.site.register(Dog)
admin.site.register(DogOwner)
admin.site.register(Tag)
admin.site.register(Article)