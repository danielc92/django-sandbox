from django.shortcuts import render

# Create your views here.
def view_dogs(request):

    data = Dog.objects.all()

    context = {'title':'Dogs list view',
               'data':data}

    return render(request, 'dog_list.html', context)