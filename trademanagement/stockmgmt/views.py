# from stockmanagement.stockmgmt.models import Stock
from typing import List
from django.db.models.fields import PositiveBigIntegerField

from django.views.generic.edit import UpdateView
from .models import Broker, Stock
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from   django.urls import reverse_lazy


# Create your views here.
                                  ##  sds  D S
## function based view
def home(request):
    stocks = Stock.objects.all( )
    context= {'stocks': stocks, 'yo':'yoyo'}
    return render(request, 'home.html', context)

class StockDetail(DetailView):
    model = Stock
    template_name = 'detail.html'
    context_object_name = 'stock'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):

        context= super(StockDetail,self).get_context_data(**kwargs)
        print('lkjjjjjjjjjjjjjjjjjjjjjjjjjj:', context)
        print('jjjjjlllllllllllll:',self.object)
        context['broker']= Broker.objects.filter(stocks= self.object)
        return context

class StockCreate(CreateView):
    model = Stock
    template_name = 'stockcreate.html'
    fields = '__all__'
    success_url= reverse_lazy('home')

                                  ##  sds  D S
def UpdateStock(request, pk):
    stock= get_object_or_404(Stock, pk= pk)
    print('stock:-----',stock)
    if request.method == 'POST':
        name= request.POST['name']
        ltp= request.POST['Ltp']
        Quantity=request.POST['Quantity']
        stockupdating= Stock.objects.filter(pk= pk)
        print('stockbefore update:', stockupdating)
        stockupdating.update(name= name, ltp= ltp, quantity= Quantity)
        print('stockupdating:------------', stockupdating)
        return redirect('home')
    else: 
        context= {'stock': stock}
        return render (request, 'update.html' , context )
    
class StockUpdate(UpdateView):
    model = Stock
    template_name = 'updatebyclass.html'
    fields= '__all__'
    pk_url_kwarg = 'prik'
    success_url= reverse_lazy('home')
                                  ##  sds  D S

def DeleteStock(request, pk):
    stock = get_object_or_404(Stock, pk= pk)
    if request.method == 'POST':
        stock.delete()
        #Stock.objects.filter(pk= pk).delete()
        return redirect('home')
    else:
        return render (request, 'delete.html' , {'stock':stock} )

    



