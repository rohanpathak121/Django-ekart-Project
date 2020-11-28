from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product
from carts.models import Cart

class ProductDetailView(DetailView):
    template_name="products/detail.html"
    model=Product

    def get_context_data(self,*args,**kwargs):
        context=super(ProductDetailView,self).get_context_data()
        cart_obj=Cart.objects.new_or_get(self.request)

        context['in_cart']=context['object'] in cart_obj.products.all()
        return context

# Create your views here.
#class based view
class ProductListView(ListView):
    template_name="products/list.html"
    model=Product


    # def get_context_data(self,*args,**kwargs):
        #object_list=Product.object.filter(active=True)
       # return {'object_list':object_list}


#function based view
def product_list(request):
    productList=Product.objects.filter(active=True)
    context={'object_list':productList}
    return render(request,"products/list.html",context)


