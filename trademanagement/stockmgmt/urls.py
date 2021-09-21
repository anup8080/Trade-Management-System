from functools import update_wrapper
from django.conf import urls
from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views
from .views import *
                                  ##  sds  D S

urlpatterns= [
    path('', views.home, name='home'),
    path('detail/<int:pk>', StockDetail.as_view(), name='stockdetail'),
    path('create/', StockCreate.as_view(), name='stockcreate' ),
    path('update/<int:pk>', views.UpdateStock, name='updatestock' ),
    path('updatebyclassd/<int:prik>', StockUpdate.as_view(), name='updatestockbyclass'),
    path('delete/<int:pk>', views.DeleteStock, name='delete'),       
]         
