from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dog, DogOwner, Article
from .forms import DogForm, ArticleForm

# Create your views here.
def owner_list(request):

    data = DogOwner.objects.all()

    context = {'title': 'Dog Owner list view',
                'data': data}

    return render(request, 'owner_list.html', context)

def dog_list(request):

    data = Dog.objects.all()

    context = {'title':'Dogs list view',
               'data':data}

    return render(request, 'dog_list.html', context)


def article_list(request):

    data = Article.objects.all()

    context = {'title':'Article list view',
               'data':data}

    return render(request, 'article_list.html', context)


def dog_create(request):

    if request.method == "POST":
        
        form = DogForm(request.POST, request.FILES)

        if form.is_valid():
            
            form.save()

            return redirect('success')

    else:
        form = DogForm()

    context = {'form': form, 'title': 'Create a dog form.'}

    return render(request, 'create.html', context)

def article_create(request):

    if request.method == "POST":

        form = ArticleForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('success')

    else:
        form = ArticleForm()

    context = {'form': form, 'title': 'Create an article'}

    return render(request, 'create.html', context)

def success(request):

    return render(request, 'success.html', {})

def mce_create(request):

    if request.method == 'POST':
        form = MceForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('success')
    else:
        form = MceForm()

    context = {'form': form, 'title': 'Create mce content'}

    return render(request, 'create.html', context)