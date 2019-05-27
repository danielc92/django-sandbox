from .models import Dog, Article
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomRegisterForm(UserCreationForm):

    # Adding a mandatory email field to the UserCreationForm
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['dog_name', 'dog_image', 'owner_id']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['article_name', 'article_content', 'tags']