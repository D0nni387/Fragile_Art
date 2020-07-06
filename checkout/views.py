from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from store.models import Product


def checkout(request):
    """A View to return the checkout form"""
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Errrr there is nothing in here at all!")
        return redirect(reverse('store'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51GqJ5EHKfLOwRnJ3XFXbQ8xlzVlnViREL22CaqdLVUKpK4noXLjrl6HawbOUuIXQUZw3gg1Ib8pPuvIqQk4Pag1D00mheCMCdh'
    }

    return render(request, template, context)