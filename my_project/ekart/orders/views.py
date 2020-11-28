from django.shortcuts import render
from carts.models import Cart
from billing.models import BillingProfile
from .models import Order
from accounts.forms import LoginForm
from addresses.forms import AddressForm
from addresses.models import Address


def success(request):
    pay_id = request.POST.get("razorpay_payment_id")
    orderid = request.POST.get("orderid")
    cart_obj = Cart.objects.new_or_get(request)
    cart_obj.active = False
    # cart_obj - active = True/False
    cart_obj.save()
    # get order_obj
    order_obj = Order.objects.filter(order_id = orderid).first()
    # order_obj - status - paid
    order_obj.status = "paid"
    #order_obj add 
    order_obj.razorpay_id = pay_id
    order_obj.save()
    # delete cart from session
    del request.session['cart_id']
    context = {'oid':orderid, 'pid':pay_id}
    return render(request, "orders/success.html", context)

def create_order(request):
    login_form=LoginForm()
    address_form=AddressForm()
    cart_obj = Cart.objects.new_or_get(request)
    context = {'cart_obj' : cart_obj,'login_form':login_form,'address_form':address_form}
    if request.user.is_authenticated:
        bill_obj = BillingProfile.objects.get_or_new(request)
        context['bill_obj'] = bill_obj
        add_list=Address.objects.filter(billing_profile=bill_obj)
        if add_list.count() > 0:
            context['add_list']=add_list
        order_obj = Order.objects.new_or_get(bill_obj, cart_obj)
        context['order_obj']=order_obj
        print("From orders/views.py : create_order: ", order_obj)
    return render(request, "orders/placeorder.html", context)
