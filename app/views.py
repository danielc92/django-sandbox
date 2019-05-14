from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dog, DogOwner
from .forms import DogForm

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


def dog_create(request):

    if request.method == "POST":
        form = DogForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            print('The form data has been cleaned:', cd)
            Dog.objects.create(**cd)
            return HttpResponse('<code>success</code>')

    else:
        form = DogForm()

    context = {'form': form, 'title': 'Create a dog form.'}

    return render(request, 'create.html', context)