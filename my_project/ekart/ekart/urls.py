"""ekart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts.views import register_page,login_page,logout_page
from .views import home_page,home_page1,home_page2,home_page3,about_page,contact_us
from django.conf.urls.static import static
from django.conf import settings 

# . mean accses folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home_page,name="home"),
    #path("home1/",home_page1),
    path("home2/",home_page2),
    path("home3/",home_page3),
    path("bdy",about_page,name="about"),
    path("bddy",contact_us,name="contact"),
    path("register/",register_page,name="register"),
    path("login/",login_page,name="login"),
    path("logout/",logout_page,name="logout"),
    #include take 2 parameter
    #1 tuple filename url ,app name
    #2 namespace nickname to app here we use product we can use anything
    path("product/",include(('products.urls','products'),namespace='product')),
    path("cart/", include(('carts.urls', 'carts'), namespace="cart")),
    path("order/",include(('orders.urls','orders'),namespace="order")), 
    path("address/",include(("addresses.urls",'addresses'),namespace="address")),

]

urlpatterns=urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns=urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



