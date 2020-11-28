from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model=Product

    list_display=['id','title','price','slug']
    search_fields=['id','title','price','slug','description']

admin.site.register(Product,ProductAdmin)    

