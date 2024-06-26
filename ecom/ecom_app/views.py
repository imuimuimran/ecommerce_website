from django.shortcuts import render
from urllib import request
from django.views import View
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "ecom_app/home.html")

class CategoryView(View):
    def get(self, request, val):
        return render(request, "ecom_app/category.html", locals())