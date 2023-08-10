from django.db import models

class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.dish_name

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.customer_name

class Menu(models.Model):
    dish = models.OneToOneField(Dish, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField()

    def __str__(self):
        return self.dish.dish_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status_choices = (
        ('received', 'Received'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready for Pickup'),
        ('delivered', 'Delivered')
    )
    status = models.CharField(max_length=20, choices=status_choices, default='received')
    dishes = models.ManyToManyField(Dish, through='OrderDish')

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer}, Status: {self.status}"

class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_subtotal(self):
        return self.dish.price * self.quantity



