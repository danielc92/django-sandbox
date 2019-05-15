from django.forms import ModelForm
from .models import Dog, Article


class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['dog_name', 'dog_image', 'owner_id']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['article_name', 'article_content', 'tags']

