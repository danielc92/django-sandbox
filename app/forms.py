from django import forms
from .models import Dog

class DogForm(models.ModelForm):
    class Meta:
        model = Dog