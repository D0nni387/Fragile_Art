from django.shortcuts import render, redirect, get_object_or_404, reverse

from store.models import Product

# Create your views here.

def basket(request):
    """A View to return the users basket"""
    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ Add the requested item to the basket"""

    item = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)

def update_basket(request, item_id):
    """ A View to update the basket with """

    item = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop[item_id]

    request.session['basket'] = basket
    return redirect(redirect_url)