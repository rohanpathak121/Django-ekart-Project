import random, string
from django.utils.text import slugify
# Atta Maggi - atta-maggi

#a6jhj89bc
def random_string_generator(size=10, chars=string.ascii_lowercase+string.digits):
    return "".join(random.choice(chars) for _ in range(size))
    # s = ""
    # for i in range(size):
    #     s = s + random.choice(chars)
    # return s

def unique_orderid_generator(instance,new_orderid=None):
    Klass=instance.__class__
    orderid=random_string_generator().upper()
    # cheaking if orderid is in databases
    check=Klass.objects.filter(order_id=orderid).exists()
    if check:
        new_orderid="{}{}".format(orderid,random_string_generator(size=1))
        return unique_orderid_generator(instance,new_orderid)
    return orderid

def unique_slug_generator(instance, new_slug=None):
    # user is slug - consider it
    # user has not entered slug then title as slug
    # slug value already exists - function will call itself.
    if new_slug is not None:
        slug = new_slug
    elif instance.slug is not None:
        slug = slugify(instance.slug)
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
# Product.objects.filter(slug)
# slug = maggi # id = 1
# select * from products where slug="maggi" and not id=1
    qs_exists = Klass.objects.filter(slug=slug).exclude(id=instance.id).exists()
    if qs_exists:#True
        # slug=maggi random=12rg # maggi-12rg
        new_slug = "{}-{}".format(slug,random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug





