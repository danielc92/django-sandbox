from django.forms import ModelForm
from .models import Dog, Article
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['dog_name', 'dog_image', 'owner_id']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['article_name', 'article_content', 'tags']

