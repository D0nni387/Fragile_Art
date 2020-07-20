from django.shortcuts import render


# Create your views here.

def user(request):
    """A View to display a users profile"""

    context = {
        
    }

    return render(request, 'users/user.html')