from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from .forms import AddressForm
from .models import Address
from billing.models import BillingProfile
from carts.models import Cart
from orders.models import Order
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView

# model, fields - modelname_form.html

class AddressUpdate(UpdateView):
    model = Address
    form_class = AddressForm


class AddressCreate(CreateView):
    model = Address
    #fields=['address_to','address_line_1','address_line_2','city','state','country','pin_code']
    form_class = AddressForm

    def post(self, *args, **kwargs):
        form = AddressForm(self.request.POST)
        if form.is_valid():
            add_obj=form.save(commit=False)
            add_obj.billing_profile=BillingProfile.objects.get_or_new(self.request)
            add_obj.save()
            return redirect(add_obj.get_absolute_url())
        return render(self.request, "addresses/address_form.html", {'form':form})



class AddressDetail(DetailView):
    model=Address
    template_name="addresses/detail.html"


class AddressList(ListView):
    model=Address
    template_name="addresses/list.html"

    def get_context_data(self, *args, **kwargs):
        context={'object_list': Address.objects.get_user_address(self.request)}
        return context

def create_address(request):
    redirect_url=request.POST.get('red_url') or None
    addressForm=AddressForm(request.POST or None)
    if addressForm.is_valid():
        add_obj=addressForm.save(commit=False)
        add_obj.billing_profile=BillingProfile.objects.get_or_new(request)
        add_obj.save()
        attach_address(request,add_obj)
        if redirect_url:
            if is_safe_url(redirect_url,request.get_host()):
                return redirect(redirect_url)
    return redirect("home")          

def adding_selection(request):
    redirect_url=request.POST.get('red_url') or None
    addid=request.POST.get("add_detail")
    add_obj=Address.objects.filter(id=addid)
    attach_address(request,add_obj)
    if redirect_url:
        if is_safe_url(redirect_url,request.get_host()):
            return redirect(redirect_url)
    return redirect("home")



def attach_address(request,add_obj):
    cart_obj=Cart.objects.new_or_get(request)
    order_obj=Order.objects.new_or_get(add_obj.billing_profile,cart_obj)
    order_obj.address=add_obj
    order_obj.save()        


# Create your views here.
