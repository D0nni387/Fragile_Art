from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.basket, name='basket'),
    path('add/<item_id>', views.add_to_basket, name='add_to_basket'),

]