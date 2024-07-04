from django.shortcuts import render, redirect
from django.views import View
from . models import products
from django.db.models import Count
from . forms import CustomerRegistrationForm, CustomerProfileForm, Customer
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
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            division = form.cleaned_data['division']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, division=division, zipcode=zipcode)
            reg.save()
            
            messages.success(request, "Congratulations! Profile save successfully.")
        else:
            messages.warning(request, "Invalid input data")
            
        return render(request, "ecom_app/profile.html", locals())
    

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, "ecom_app/address.html", locals())

class UpdateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, "ecom_app/update_address.html", locals())
        
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.division = form.cleaned_data['division']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Congratulations! Profile update successfully.")
        else:
            messages.warning(request, "Invalid input data")
        return redirect("address")
    