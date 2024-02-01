from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Inventory
from .models import order as Order
from .forms import InventoryForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
#from elasticapm.contrib.flask import ElasticAPM
#import elasticapm
#mport random
#import logging
#import time

#logging disable flask logger
#handler = logging.getLogger('haidar')
#logger = logging.getLogger("app")
#logger.setLevel(logging.ERROR)
#logger.setLevel(logging.DEBUG)

#log to file 
#handler = logging.FileHandler(filename='/Users/Haidar/Desktop/App/Logs/log1.log')
#logger.addHandler(handler)

# Create your views here.

# here we build the index response view
@login_required
def index(request):
    return render(request, 'dashboard/index.html')

# here we build the staff response view
@login_required
@user_passes_test(lambda u: u.is_superuser)
def staff(request):
    workers = User.objects.all()
    context = {
        'workers':workers
    }
    return render(request, 'dashboard/staff.html', context)

# here we are building a view for staff details for admin
@login_required
@user_passes_test(lambda u: u.is_superuser)
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)

 # here we build the product response view

@login_required
@user_passes_test(lambda u: u.is_superuser)
def inventory(request):
    #logger.info("Received Request")
    #table_name = Inventory._meta.db_table
    items = Inventory.objects.all() # here I use ORM
    #items = Inventory.objects.raw('SELECT * FROM dashboard_Inventory')
    #logger.info("connecting to database")
    if request.method =='POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-inventory')
            #return redirect('BAD Request')
    else:
        form = InventoryForm
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/inventory.html', context)
    

 # here we build the Order response view
@login_required
@user_passes_test(lambda u: u.is_superuser)
def order(request):
    orders = Order.objects.all()
    context = {
        'orders':orders,
    }
    return render(request, 'dashboard/order.html', context)


# delete inventory
@login_required
@user_passes_test(lambda u: u.is_superuser)
def inventory_delete(request, pk):
    item = Inventory.objects.get(id=pk)
    if request.method=='POST':
        item.delete() 
        return redirect('dashboard-inventory')
    #else: 
        #return ('hi my name is bad user')
    return render(request, 'dashboard/inventory_delete.html')

#userVariable = @user_passes_test(lambda u.is_staff)
# update inventory
@login_required
@user_passes_test(lambda u: u.is_superuser)
def inventory_update (request, pk):
   item = Inventory.objects.get(id=pk)
   #if userVariable == 'True':
   if request.method == 'POST':
       form = InventoryForm(request.POST, instance=item)
       if form.is_valid():
           form.save()
           return redirect('dashboard-inventory')
   else:
       form = InventoryForm(instance=item)
   context={
       'form': form,
   }
   return render (request, 'dashboard/inventory_update.html', context) 
      # else:
       #return render('nothing found')
