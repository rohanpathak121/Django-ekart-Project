from django.db import models
from billing.models import BillingProfile
from django.urls import reverse

# Create your models here.

class AddressQuerySet(models.query.QuerySet):
    def user_address(self,request):
        return self.filter(billing_profile__user__username__iexact=request.user.username)

class AddressManager(models.Manager):
    def get_queryset(self):
        return AddressQuerySet(self.model,using=self._db)
    def get_user_address(self,request):
        return self.get_queryset().user_address(request)     

class Address(models.Model):
    billing_profile=models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
    address_to=models.CharField(max_length=200)
    address_line_1=models.CharField(max_length=120)
    address_line_2=models.CharField(max_length=120)
    city=models.CharField(max_length=120)
    state=models.CharField(max_length=120)
    country=models.CharField(max_length=120,default="India")
    pin_code=models.IntegerField()

    objects=AddressManager()
    
    def __str__(self):
        return self.address_to + ":" + self.address_line_1

    def get_address(self):
        address=self.address_to + "\n" + self.address_line_1 +",\n" + self.address_line_2 +", \n"+self.city+", \n"+self.state+", \n"+self.country+" - " +str(self.pin_code) 
        return address  

    def get_absolute_url(self):
        return reverse("address:detail",kwargs={'pk':self.id})

    def get_update_url(self):
        return reverse("address:update",kwargs={'pk':self.id})
        




