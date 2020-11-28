from django.db import models
from carts.models import Cart
from billing.models import BillingProfile
from decimal import Decimal
from django.db.models.signals import pre_save
from products.utils import unique_orderid_generator
from addresses.forms import Address

# Create your models here.

ORDER_STATUS_CHOICES=(
    #('stored in db,'Viewed Form'')
    ('created','Created'),
    ('paid','Paid'),
    ('refunded','Refunded'),
    ('shipped','Shipped'),
    ('delivered','Delivered'),
    ('cancel','Cancel'),

)

class OrderManager(models.Manager):
    def new_or_get(self,bill_obj,cart_obj):
        order_obj=self.get_queryset().filter(cart=cart_obj,billingProfile=bill_obj,status="created").first() or None
        if order_obj is None:
            order_obj=self.get_queryset().create(cart=cart_obj,billingProfile=bill_obj)
        order_obj.update_total(cart_obj.total)
        return order_obj    



class Order(models.Model):
    order_id=models.CharField(max_length=120,blank=True,null=True,unique=True)
    #billing profile--FK--Every User will have one billing proifle --Rozar pay--customer Id from RP
    #address--FK(ForeignKey)

    billingProfile=models.ForeignKey(BillingProfile,on_delete=models.PROTECT)
    
    address=models.ForeignKey(Address,null=True,blank=True,on_delete=models.CASCADE)

    cart=models.ForeignKey(Cart,on_delete=models.PROTECT) 

    #enum is RDBMS choice in ORM
    status=models.CharField(default="created",max_length=25,choices=ORDER_STATUS_CHOICES)

    #cart Total
    order_total=models.DecimalField(max_digits=8,decimal_places=2,default=0)

    #Rozer pay ---transactoin id rozerpay_id
    razorpay_id = models.CharField(max_length = 120, null = True, blank = True)

    objects=OrderManager()
    
    def __str__(self):
        return self.order_id


    def update_total(self,cart_total):
        if self.order_total!=cart_total:
            self.order_total=cart_total
            
            self.total=round(self.order_total*Decimal(1.18),2)
            self.save()    

def order_orderid_pre_save_receiver(sender,instance,*args,**kwargs):
    if instance.order_id == "" or instance.order_id is None:
        instance.order_id=unique_orderid_generator(instance)
pre_save.connect(order_orderid_pre_save_receiver,sender=Order)                  
