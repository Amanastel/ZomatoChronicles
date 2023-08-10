from django import forms
from .models import Dish, Menu, Customer

class AddDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['dish_name', 'price', 'availability']

class AddDishToMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['dish', 'description']


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'address', 'phone_number']
