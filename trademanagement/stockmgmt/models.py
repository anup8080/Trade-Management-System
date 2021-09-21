from django.db import models
from django.contrib.auth.models import User, auth 
from django.conf import settings
from django.db.models.deletion import CASCADE

from django.shortcuts import render, redirect 
from  django.shortcuts import reverse



# Create your models here.


class Stock(models.Model):
    name= models.CharField(max_length=25)
    ltp= models.IntegerField()
    quantity= models.IntegerField()

    def __str__(self):
        return f'{self.name}'

    # def get_absolute_url(self):
    #     print("!!!!!!!!!!!!!!!! absolute url",self.slug)
    #     return reverse("home")

class Broker(models.Model):
    number= models.IntegerField()
    name= models.CharField(max_length=25)
    stocks= models.ManyToManyField(Stock, related_name='brostock')

    def __str__(self):
        return f'{self.name}+{self.number}'

class Customer(models.Model):
    user= models.OneToOneField(User, on_delete= CASCADE, null= True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
	#profile_pic = models.ImageField(default="profile_pic.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    brokers = models.ManyToManyField(Broker, related_name='cusbro')
    stocks = models.ManyToManyField(Stock, related_name='cusstock', null=True, blank= True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
	    return self.name

    
