from django.db import models
from django.contrib.auth.models import User
from django.db.models import F

# Create your models here.


class Inventory(models.Model):
    Name = models.CharField(max_length=100, null=True)
    SN = models.CharField(max_length=20, null=True)
    Vendor = models.CharField(max_length=100, null=True)
    Quantity = models.PositiveIntegerField(null=True)
    Price = models.PositiveBigIntegerField(null=True)
    
    #change name of model on admin dashboard
    class Meta:
        # I forced a change of name on db name in the variable db_table
        db_table = 'Inventory'
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventory System'
   
    #table layout configuration
    def __str__(self):
        return f'{self.Name}   -   {self.Quantity}   -   {self.Vendor}'

#Cost Calculation
  #  @property
   # def amount(self):
    #    return self.Quantity * self.Price

CATEGORY = (
    ('category', 'Quote'),
    ('category', 'Approved Orders'),
)

#binding database models for inventory, orders, and staff
class order(models.Model):
    Product = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True)
    Staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveBigIntegerField(null=True)
    Price = models.PositiveBigIntegerField(null=True)
    Category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    date = models.DateTimeField(auto_now=True)

    #order layout configuration
    def __str__(self):
        return f'{self.Product} ordered by {self.Staff.username}'
    
    class Meta:
        verbose_name_plural = 'Order System'