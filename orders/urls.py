from django.contrib import admin
from django.urls import path, include
from shop import views as shop
from users import views as users
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'orders'

urlpatterns = [
    path('create_order/', views.create_order, name="create_order"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
['Nothing', 'will', 'work', 'unless', 'you', 'do']
