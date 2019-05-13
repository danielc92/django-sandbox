from django.shortcuts import render
from .models import Dog, DogOwner


# Create your views here.
def dog_list(request):

    data = Dog.objects.all()

    context = {'title':'Dogs list view',
               'data':data}

    return render(request, 'dog_list.html', context)