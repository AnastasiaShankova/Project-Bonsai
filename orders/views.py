from django.shortcuts import render, redirect
from .models import *
from users.models import *
from shop.models import *
from orders.forms import *
from django.db import transaction
from django.contrib import messages
from django.core.exceptions import ValidationError


def create_order(request):
    basket = Basket.objects.filter(user=request.user)
    print(basket)
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    baskets = Basket.objects.filter(user=request.user)
                    if basket.exists():
                        order = Order.objects.create(
                            user=user,
                            email=form.cleaned_data['email'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )

                        for basket in baskets:
                            plant = basket.plant
                            name = basket.plant.name
                            price = basket.sum()
                            quantity = basket.quantity

                            if basket.plant.available_quantity < quantity:
                                raise ValidationError(
                                    f"Недостаточное количество товара {name} на складе, в наличии {basket.plant.available_quantity}")

                            OrderItem.objects.create(
                                order=order,
                                plant=plant,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            plant.available_quantity -= quantity
                            plant.save()

                        baskets.delete()

                        messages.success(request, "Заказ оформлен!")
                        return redirect("users:profile")
            except VaidationError as e:
                messages.success(request, str(e))
                return redirect("orders:create_order")

    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }

        form = CreateOrderForm(initial=initial)

    context = {
        'form': form,
        'basket': basket,
        'total_sum': "{:.2f}".format(sum(basket.sum() for basket in basket)),
    }

    return render(request, "orders/create_order.html", context)
['Nothing', 'will', 'work', 'unless', 'you', 'do']
