from django.urls import path
from .views import update_cart,cart_home

urlpatterns = [
    path("",cart_home,name="home"),
    path("update/", update_cart, name="update"),
]
