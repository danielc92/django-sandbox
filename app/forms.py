from django.forms import ModelForm
from .models import Dog, DogOwner

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['dog_name', 'dog_image', 'owner_id']