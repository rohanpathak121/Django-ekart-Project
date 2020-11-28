from django.db import models
#from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

from django.db.models.signals import post_save,pre_save
import razorpay
client = razorpay.Client(auth=("rzp_test_jmQVtMY6NhppaP", "qWqJIYIrdnzo7LaQd0ZGGnqH"))


# user ModelManager outside the class --model objects
# user 

class BillingManager(models.Manager):
    def get_or_new(self,request):
        if request.user.is_authenticated:
            bill_obj=self.get_queryset().filter(user=request.user).first() or None
            if bill_obj is None:
                bill_obj=self.get_queryset().create(user=request.user,email=request.user.email)
        return bill_obj

# Create your models here.

class BillingProfile(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    email=models.EmailField()
    active=models.BooleanField(default=True)
    createdDate=models.DateTimeField(auto_now_add=True)
    updatedDate=models.DateTimeField(auto_now=True)
#customer_id-RP customerid
    customer_id = models.CharField(max_length = 120, null = True, blank = True)

    objects=BillingManager()

    def __str__(self):
        return str(self.user)+"-"+self.email

def user_created_receiver(sender,instance,created,*args,**kwargs):
    if created and instance.email:
        BillingProfile.objects.create(user=instance,email=instance.email)

post_save.connect(user_created_receiver,sender=User)


def customer_id_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.customer_id:
        data = {
            "name":instance.user.full_name,
            "email":instance.email,
            "contact":instance.user.mobile
        }
        customer = client.customer.create(data=data)
        instance.customer_id = customer.get("id")


pre_save.connect(customer_id_pre_save_receiver, sender = BillingProfile)