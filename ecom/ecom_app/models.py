from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (
    ('CR', 'Crud'),
    ('ML', 'Milk'),
    ('Ls', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
)

DIVI_CHOICES = (
    ('DHK', 'Dhaka'),
    ('CTG', 'Chitagong'),
    ('SLT', 'Sylhet'),
    ('KHL', 'Khulna'),
    ('RAN', 'Rangpur'),
    ('RAJ', 'Rajshahi'),
    ('BRS', 'Barishal'),
    ('MYN', 'Mymanshing'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    product_app = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_img = models.ImageField(upload_to='product')
    
    def __str__(self):
        return self.title
    

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=60)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    division = models.CharField(choices=DIVI_CHOICES, max_length=100)
    def __str__(self):
        return self.name
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    