from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#This will allow us to import libraries from the views.py in the current directory
from . import views

#here we define the urls that we are handling in the views.p
urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('inventory/', views.inventory, name='dashboard-inventory'),
    path('order/', views.order, name='dashboard-order'),
    path('inventory/delete/<int:pk>/', views.inventory_delete, name='dashboard-inventory-delete'),
    path('inventory/update/<int:pk>/', views.inventory_update, name='dashboard-inventory-update'),
]

urlpatterns += staticfiles_urlpatterns()