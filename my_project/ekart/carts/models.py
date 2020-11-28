from django.db import models
from products.models import Product
#from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from decimal import Decimal
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

# Relationship    1 to 1 , 1 to M , M to M

class CartManager(models.Manager):
    def new_or_get(self, request):
        cartid = request.session.get('cart_id' or None)
        # When cartid is available in session
        if cartid:
            cart_obj = Cart.objects.filter(id=cartid, active=True).first()
        # if cart id is not available in session but a user has a cartid assigned to him or her then load that
        elif request.user.is_authenticated:
            cart_obj = Cart.objects.filter(user=request.user, active=True).first() or None
            if cart_obj is None:
                cart_obj = Cart.objects.create(user=request.user)
            request.session['cart_id'] = cart_obj.id
        # user not logged in nor there is cart id in session
        else:
            cart_obj = Cart.objects.create()
            request.session['cart_id'] = cart_obj.id
        request.session['cart_count'] = cart_obj.products.all().count()
        return cart_obj    

class Cart(models.Model):
    products=models.ManyToManyField(Product,blank=True)

    #CASCADE=delete the requred records
    #protect =dont delete the record
    user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    active=models.BooleanField(default=True)
    sub_total=models.DecimalField(max_digits=7,decimal_places=2,default=0)
    total=models.DecimalField(max_digits=7,decimal_places=2,default=0)
    createdDate=models.DateField(auto_now_add=True)
    updatedDate=models.DateField(auto_now=True)

    objects=CartManager()

    def __str__(self):
        return str(self.id)
def m2m_changed_product_receiver(sender,instance,*args,**kwargs):
    if instance.products.all().count()>0:
        instance.sub_total=0
        for prod in instance.products.all():
            instance.sub_total+=prod.price       
        if instance.sub_total< Decimal(500):
            instance.total=instance.sub_total+Decimal(80)
        else:
            instance.total=instance.sub_total
        instance.save()
m2m_changed.connect(m2m_changed_product_receiver,sender=Cart.products.through)                    