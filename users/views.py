from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import ProfileForm


# Create your views here.

def user(request):
    """A View to display a users profile"""
    user = get_object_or_404(UserProfile, user=request.user)

    form = ProfileForm(instance=user)
    orders = user.orders.all()

    template = 'users/user.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)