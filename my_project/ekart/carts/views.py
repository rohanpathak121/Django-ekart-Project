from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart

def cart_home(request):
    cart_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {'object':cart_obj})

def update_cart(request):
    # User click on Add to Cart
    # 1. create a cart object and store cart id in session
    # 2. load the product object
    # 3. Cart object I will either add or remove the product
    if request.method == "POST":
        prodid = request.POST.get('prodid')
        prod_obj = Product.objects.filter(id=prodid).first()
        #check for cart_id in session
        # if request.session.get("cart_id"):
        #     cart_obj = Cart.objects.filter(id=request.session.get("cart_id")).first()
        #     print(cart_obj)
        # else:
        #     cart_obj = Cart.objects.create()
        #     request.session['cart_id'] = cart_obj.id
        cart_obj = Cart.objects.new_or_get(request)
        
        if prod_obj in cart_obj.products.all():
            cart_obj.products.remove(prod_obj)
        else:
            cart_obj.products.add(prod_obj)
    # return redirect(prod_obj.get_detailview_url())
    return redirect("cart:home")