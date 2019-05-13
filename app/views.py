from django.shortcuts import render
from .models import Dog, DogOwner
from .forms import DogForm

# Create your views here.
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
            print(cd)
            return 'Success'

    else:
        form = DogForm()

    context = {'form': form, 'title': 'Create a dog form.'}

    return render(request, 'create.html', context)