from django.contrib import admin

# Register your models here.
from .models import Dog, Desk, Occupant, DogOwner, Tag, Article

admin.site.register(Dog)
admin.site.register(DogOwner)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Occupant)
admin.site.register(Desk)