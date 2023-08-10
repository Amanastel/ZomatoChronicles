"""
URL configuration for zomatoCharocic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
   path('', views.index, name='index'),
   path('view_menu/', views.view_menu, name='view_menu'),
   path('add_dish/', views.add_dish, name='add_dish'),
   path('add_dish_to_menu/', views.add_dish_to_menu, name='add_dish_to_menu'),
   path('remove_dish/<int:dish_id>/', views.remove_dish, name='remove_dish'),
   path('update_availability/<int:dish_id>/', views.update_availability, name='update_availability'),
   path('add_customer/', views.add_customer, name='add_customer'),
   path('view_customers/', views.view_customer_list, name='view_customers'),
   path('add-order/', views.add_order, name='add_order'),
   path('view-order-history/', views.view_order_history, name='view_order_history'),
   path('view_customer_list/', views.view_customer_list, name='view_customer_list'),
   path('view-customer-order-history/<int:customer_id>/', views.view_customer_order_history, name='view_customer_order_history'),
]
