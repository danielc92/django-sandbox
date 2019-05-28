from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dog, DogOwner, Article, Desk, Occupant
from .forms import DogForm, ArticleForm, CustomRegisterForm

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

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


# Function to fetch articles, convert to json format for redis storage
def return_article_data():
    data = Article.objects.all()
    
    data_json = [{'id': a.id, 
                  'article_content': a.article_content, 
                  'article_ct_date': a.article_ct_date,
                  'article_name': a.article_name,
                  'article_tags': [t.tag_name for t in a.tags.all()]} for a in data]
    return data_json


def article_list(request):

    # if 'articles' in cache:
    #     data = cache.get('articles')
    # else:
    #     data = return_article_data()
    #     cache.set('articles', data, timeout=CACHE_TTL)

    data = return_article_data()

    u = request.user

    context = {'title':'Article list view',
               'data':data,
               'u':u}

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


def bulmafy_form(form):
    form = form.as_p()
    form = form.replace('<label', '<label class="label"')
    form = form.replace('</select>', '</select></div>')
    form = form.replace('<select', '<div class="select is-multiple"> <select')
    form = form.replace('<span','<p class="help"><span')
    form = form.replace('</span>', '</span></p>')
    return form


@login_required
def article_create(request):

    if request.method == "POST":

        form = ArticleForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('success')

    else:
        form = ArticleForm()
        form = bulmafy_form(form)

    context = {'form': form, 'title': 'Create an article'}

    return render(request, 'create.html', context)


def success(request):

    return render(request, 'success.html', {})


def setsession(request):
    request.session['username'] = 'danielc92'

    return HttpResponse('Session has been set.')


def getsession(request):
    
    username = request.session.get('username')
    
    if username:

        return HttpResponse('Session has been requested. Username is {}'.format(username))
    else:

        return HttpResponse('You need to set a session...')


def accounts_register(request):

    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print('{} has registered successfully'.format(username))
            return redirect('success')
    else:
        form = CustomRegisterForm()
        form = bulmafy_form(form)
    
    context = {'form': form}

    return render(request, 'create.html', context)

@login_required
def accounts_change(request):

    errors = None

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            print('Form is valid!')
            print(form.cleaned_data)
            form.save()
            return redirect('success')
        else:
            errors = 'Password does not match requirements'
            print(errors)
    else:
        form = PasswordChangeForm(request.user)
    
    form = bulmafy_form(form)
    
    context = {'form': form, 'errors': errors}

    return render(request, 'create.html', context)


class DeskView(ListView):

    model = Desk
    template_name = 'desk_list_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Desk List View'
        return context


class DeskUpdate(UpdateView):

    model = Desk
    template_name = 'desk_update_view.html'
    fields = ['desk_level', 'desk_weight', 'desk_cost', 'desk_width', 'desk_length', 'desk_occupant']

class DeskCreate(CreateView):

    model = Desk
    template_name = 'desk_create_view.html'
    fields = ['desk_level', 'desk_weight', 'desk_cost', 'desk_width', 'desk_length', 'desk_occupant']