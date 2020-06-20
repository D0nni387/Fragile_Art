from django.shortcuts import render

# Create your views here.

def store(request):
    """A View to return index page"""
    return render(request, 'store/store.html')