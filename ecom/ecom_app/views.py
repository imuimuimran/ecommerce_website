from django.shortcuts import render
from django.views import View
from . models import products
from django.db.models import Count
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "ecom_app/home.html")

def about(request):
    return render(request, "ecom_app/about.html")

def contact(request):
    return render(request, "ecom_app/contact.html")

class CategoryView(View):
    def get(self, request, val):
        product = products.objects.filter(category=val)
        title = products.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request, "ecom_app/category.html", locals())
    
class CategoryTitle(View):
    def get(self, request, val):
        product = products.objects.filter(title=val)
        title = products.objects.filter(category=product[0].category).values('title')
        return render(request, "ecom_app/category.html", locals())
    
class ProductDetail(View):
    def get(self, request, pk):
        product = products.objects.get(pk=pk)
        return render(request, "ecom_app/product_detail.html", locals())
    
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "ecom_app/customer_registration.html", locals())
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulation!, User Register Successfully.")
        else:
            messages.warning(request, "Invalid Input Data!")
        return render(request, "ecom_app/customer_registration.html", locals())
    
class ProfileView(View):
    
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, "ecom_app/profile.html", locals())
    
    def post(self, request):
        return render(request, "ecom_app/profile.html", locals())