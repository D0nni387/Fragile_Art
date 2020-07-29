from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<item_id>', views.portfolio, name='portfolio_detail')

]