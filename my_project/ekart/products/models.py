from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(null=True,blank=True)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=10)
    image=models.ImageField(upload_to="products/",null=True,blank=True)
    active=models.BooleanField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(null=True,blank=True,auto_now=True)


    def __str__(self):
        return self.title+"@"+str(self.price)

    #def get_detailview_url(self):
        #return reverse("product:detail",kwargs={'pk':self.id}) 
           
    def get_detailview_url(self):
        return reverse("product:detail",kwargs={'slug':self.slug}) 


#outside class

def product_slug_pre_save_receiver(sender,instance,*args,**kwargs):
    instance.slug=unique_slug_generator(instance)


#assigning function to trigger
pre_save.connect(product_slug_pre_save_receiver,sender=Product)    

