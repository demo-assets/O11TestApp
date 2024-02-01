from django.contrib import admin
from .models import Inventory, order
from django.contrib.auth.models import Group

admin.site.site_header = 'Elastic Demo - Inventory APP'

#adding filter component
class InventoryAdmin (admin.ModelAdmin):
    list_display = ('Name', 'Quantity', 'Vendor')
    

class OrderAdmin (admin.ModelAdmin):
    list_display = ('Product', 'Staff', 'order_quantity' , 'Price', 'Category')
    list_filter = ['Category']
    #list_display = ('Name', 'Staff', 'order_quantity' , 'Price')

# Register your models here.
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(order, OrderAdmin)
#admin.site.unregister(Group)


