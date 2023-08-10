from django.shortcuts import render, redirect
from .models import Dish, Menu, Customer, OrderDish, Order
from .forms import AddDishForm, AddDishToMenuForm, CustomerCreateForm
# Create your views here.


def index(request):
    return render(request, 'index.html')

def view_menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'view_menu.html', {'menu_items': menu_items})

def add_dish(request):
    if request.method == 'POST':
        form = AddDishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_menu')  # Redirect to the menu page after adding the dish
    else:
        form = AddDishForm()
    return render(request, 'add_dish.html', {'form': form})

def add_dish_to_menu(request):
    if request.method == 'POST':
        form = AddDishToMenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_menu')  # Redirect to view_menu page after adding the dish
    else:
        form = AddDishToMenuForm()
    return render(request, 'add_dish_to_menu.html', {'form': form})


def remove_dish(request, dish_id):
    try:
        menu_item = Menu.objects.get(dish_id=dish_id)
        menu_item.delete()
        return redirect('view_menu')
    except Menu.DoesNotExist:
        # Handle the case when the menu item with the given dish_id doesn't exist
        return redirect('view_menu')


def update_availability(request, dish_id):
    try:
        dish = Dish.objects.get(pk=dish_id)
        # Toggle the availability status
        dish.availability = not dish.availability
        dish.save()
        return redirect('view_menu')  # Redirect back to the menu page
    except Dish.DoesNotExist:
        # Handle the case when the dish with the given dish_id doesn't exist
        return redirect('view_menu')



def add_customer(request):
    if request.method == 'POST':
        form = CustomerCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_customers')
    else:
        form = CustomerCreateForm()

    return render(request, 'add_customer.html', {'form': form})


def view_customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})


def add_order(request):
    customers = Customer.objects.all()
    dishes = Dish.objects.filter(availability=True)

    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        selected_dishes = request.POST.getlist('dishes')

        customer = Customer.objects.get(id=customer_id)
        order = Order.objects.create(customer=customer)

        for dish_id in selected_dishes:
            dish = Dish.objects.get(id=dish_id)
            order_dish = OrderDish.objects.create(order=order, dish=dish)

        return redirect('view_order_history')  # Redirect to view order history page

    return render(request, 'add_order.html', {'customers': customers, 'dishes': dishes})


def view_order_history(request):
    orders = Order.objects.all()
    return render(request, 'order_history.html', {'orders': orders})

def view_customer_order_history(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'customer_order_history.html', {'customer': customer, 'orders': orders})
