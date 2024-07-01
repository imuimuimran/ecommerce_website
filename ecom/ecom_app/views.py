from django.shortcuts import render
from django.views import View
from . models import products
from django.db.models import Count

# Create your views here.

def home(request):
    return render(request, "ecom_app/home.html")

class CategoryView(View):
    def get(self, request, val):
        product = products.objects.filter(category=val)
        title = products.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request, "ecom_app/category.html", locals())
    
class ProductDetail(View):
    def get(self, request, pk):
        product = products.objects.get(pk=pk)
        return render(request, "ecom_app/product_detail.html", locals())
        