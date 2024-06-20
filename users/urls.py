from django.contrib import admin
from django.urls import path, include
from shop import views as shop
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
['Nothing', 'will', 'work', 'unless', 'you', 'do']
