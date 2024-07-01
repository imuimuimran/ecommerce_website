from django.db import models

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

class products(models.Model):
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
    