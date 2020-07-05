from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from store.models import Product


def checkout(request):
    """A View to return the checkout form"""
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Errrr there is nothing in here at all!")
        return render(reverse('shop'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)