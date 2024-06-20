from django.contrib import admin
from django.urls import path, include
from shop import views as shop
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.main, name="index"),
    path('contacts/', views.contacts, name="contacts"),
    path('about/', views.about, name="about"),
    path('./catalog/1', views.catalog, name="catalog_1"),
    path('catalog/<int:page>/', views.catalog, name="catalog"),
    path('catalog/<int:page>/aboutplant/<int:plant_id>/',
         views.about_plant, name='aboutplant'),
    path('category/<int:choice>/<int:page>',
         views.category, name="category_id_page"),
    path('category/<int:choice>/1', views.category, name="category_id"),
    path('category/<int:choice>/<int:page>',
         views.category, name="category_id_page"),
    path('category/<int:page>/aboutplant/<int:plant_id>/',
         views.about_plant, name='aboutplant'),
    path('basket', views.basket, name="basket"),
    path('baskets/add/<int:plant_id>/', views.basket_add, name="basket_add"),
    path('catalog/<int:page>/aboutplant/<int:plant_id>/',
         views.basket_add, name="basket_add"),
    path('baskets/remove/<int:basket_id>/',
         views.basket_remove, name="basket_remove"),
    path('baskets/change_qty/<int:basket_id>/<slug:sign>/',
         views.basket_change_qty, name="basket_change_qty"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
