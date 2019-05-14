from django.forms import ModelForm
from .models import Dog, DogOwner

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['dog_name', 'owner_id']