from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import *
from users.models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import auth, messages


def main(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        context = {'basket': basket, }
        return render(request, "shop/index.html", context)
    else:
        return render(request, "shop/index.html")


def contacts(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        context = {'basket': basket, }
        return render(request, "shop/contacts.html", context)
    else:
        return render(request, "shop/contacts.html")


def about(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        context = {'basket': basket, }
        return render(request, "shop/about.html", context)
    else:
        return render(request, "shop/about.html")


def catalog(request, page=1):
    search_query = request.GET.get('search', '')
    plants = Plant.objects.filter(
        Q(name__icontains=search_query.title()) | Q(name__icontains=search_query)) if search_query else Plant.objects.all()

    categories = Category.objects.all()

    paginator = Paginator(plants, 4)
    items_paginator = paginator.get_page(page)
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        return render(request, "shop/catalog.html", {"plants": items_paginator, "categories": categories, "basket": basket, })
    else:
        return render(request, "shop/catalog.html", {"plants": items_paginator, "categories": categories, })


def category(request, choice, page=1):
    categories = Category.objects.all()
    selected_category = Category.objects.get(id=choice)

    search_query = request.GET.get('search', '')
    plants = Plant.objects.filter(Q(category=selected_category) & Q(name__icontains=search_query.title()) | Q(
        name__icontains=search_query)) if search_query else Plant.objects.all().filter(category=selected_category)

    paginator = Paginator(plants, 4)
    items_paginator = paginator.get_page(page)

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        return render(request, "shop/category.html", {'selected_category': selected_category, 'plants': items_paginator, "categories": categories, 'basket': basket, })
    else:
        return render(request, "shop/category.html", {'selected_category': selected_category, 'plants': items_paginator, "categories": categories, })


def about_plant(request, plant_id, page=1):
    selected_plant = Plant.objects.all().filter(pk=plant_id)

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        plant = Plant.objects.get(id=plant_id)
        return render(request, "shop/about_plant.html", {'selected_plant': selected_plant, 'basket': basket, 'plant': plant})
    else:

        return render(request, "shop/about_plant.html", {'selected_plant': selected_plant, })


@login_required
def basket(request):

    basket = Basket.objects.filter(user=request.user)
    context = {'basket': basket,
               'plant': Plant.objects.all(),
               'total_sum': "{:.2f}".format(sum(basket.sum() for basket in basket)),
               }

    return render(request, 'shop/basket.html', context)


@login_required
def basket_add(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    basket = Basket.objects.filter(user=request.user, plant=plant)

    if not basket.exists():
        Basket.objects.create(user=request.user, plant=plant,
                              quantity=1)

    else:
        basket = basket.first()
        if basket.quantity < basket.plant.available_quantity:
            basket.quantity += 1
            basket.save()
        else:
            messages.info(
                request, "Товар на складе закончился!")

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

        basket = Basket.objects.filter(user=request.user)

        data = {
            'message': plant.available_quantity,
            'message1': sum([qnt.quantity for qnt in basket]),
            'message2': basket.quantity_in_basket(),
        }

        return JsonResponse(data)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_change_qty(request, basket_id, sign):

    basket = Basket.objects.get(id=basket_id)

    if sign == "plus":
        if basket.quantity < basket.plant.available_quantity:
            basket.quantity += 1
            basket.save()
        else:
            messages.info(
                request, "Товар на складе закончился!")

    else:
        if basket.quantity == 1:
            basket.delete()
        else:
            basket.quantity -= 1
            basket.save()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        baskets = Basket.objects.filter(user=request.user)

        data = {
            'a_basket_id': basket_id,
            'message': sum(basket.quantity for basket in baskets),
            'message1': basket.quantity,
        }

        return JsonResponse(data)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
