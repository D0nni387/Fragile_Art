from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

def basket(request):
    """A View to return the users basket"""
    return render(request, 'basket/basket.html')