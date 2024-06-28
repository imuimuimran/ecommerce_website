from django.shortcuts import render
from django.views import View
from . models import products

# Create your views here.

def home(request):
    return render(request, "ecom_app/home.html")

class CategoryView(View):
    def get(self, request, val):
        product = products.objects.filter(category=val)
        return render(request, "ecom_app/category.html", locals())