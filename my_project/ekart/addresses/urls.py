from django.urls import path
from .views import (create_address,adding_selection,AddressList,AddressDetail,AddressCreate,AddressUpdate)

urlpatterns=[
    path("",create_address,name="create"),
    path("attach/",adding_selection,name="attach"),
    path("list/",AddressList.as_view(),name="list"),
    path("<int:pk>/",AddressDetail.as_view(),name = "detail"),
    path("create/", AddressCreate.as_view(),name= "create_add"),
    path("update/<int:pk>/", AddressUpdate.as_view(), name = "update")
]