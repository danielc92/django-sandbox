from django.contrib import admin
from django.urls import path
from app.views import (
    dog_list, 
    dog_create, 
    owner_list,
    article_create,
    article_list,
    accounts_register, accounts_change,
    setsession, getsession,
    success)

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getsession/', getsession),
    path('setsession/', setsession),
    path('dog/list/', dog_list, name='dog_list'),
    path('dog/create/', dog_create, name='dog_create'),
    path('owner/list/', owner_list, name='owner_list'),
    path('article/list/', article_list, name='article_list'),
    path('article/create/', article_create, name='article_create'),
    path('success/', success, name='success'),
    path('accounts/change/', accounts_change, name='accounts_modify'),
    path('accounts/register/', accounts_register, name='accounts_register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='accounts_login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='accounts_logout')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                        document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, 
    #                       document_root=settings.STATIC_ROOT)
