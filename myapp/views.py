""" from django import http """
""" from django.db.models.base import _Self """
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from myapp.decorators import allowed_user
from myapp.models import Contact,NProduct,Customer,shop
from myapp.forms import OrderForm,createuserform,Customerform
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from myapp.decorators import allowed_user,admin_only



# Create your views here.
@login_required(login_url="login")
# @allowed_user(allowed_rules=['admin'])
@admin_only
def index(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, "index.html")
    #return HttpResponse("This is homepage!")

@login_required(login_url="login")
@allowed_user(allowed_rules=['customer'])
def user(request):
    orders = request.user.customer.shop_set.all()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders,'total_orders':total_orders,'delivered':delivered,'pending':pending }
    return render(request, "user.html", context)

@allowed_user(allowed_rules=['admin'])
def ndetails(request):
    customers = Customer.objects.all()
    #Context = {'customers':customers, 'orders':orders}
    return render(request,"ndetails.html", context={'customers':customers})

def registration(request):
        form = createuserform()

        if request.method == "POST":
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get("username")

                messages.success(request,"Account was Created for " + username )
                return redirect("/login") 

        registerform = {'form':form}
        return render(request, "registration.html",registerform)

def loginUser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.success(request,"Name and Password are incorrect " )
            return render(request, "login.html")
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")


def about(request):
    return render(request, "about.html")

@allowed_user(allowed_rules=['admin'])
def ndetails(request):
    display_order = shop.objects.all()
    display_customer = Customer.objects.all()

    total_customer = display_customer.count()
    total_orders = display_order.count()

    delivered = display_order.filter(status='Delivered').count()
    pending = display_order.filter(status='Pending').count()

    show = {'display_order':display_order, 'display_customer':display_customer,'total_customer':total_customer,
    'total_orders':total_orders,'delivered':delivered,'pending':pending}

    return render(request,"ndetails.html", show)

@allowed_user(allowed_rules=['admin'])
def customer(request, my_id):
    customerdata = Customer.objects.get(id= my_id)

    orderdata = customerdata.shop_set.all()

    order_total = orderdata.count()

    ordercustomershow = {'customerdata':customerdata,'orderdata':orderdata, 'order_total':order_total}

    return render(request,"customer.html", ordercustomershow)


@allowed_user(allowed_rules=['admin'])
def nproduct(request):
    products = NProduct.objects.all()
    return render(request,"nproduct.html", {'products':products})

@allowed_user(allowed_rules=['admin'])
def createOrder(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ndetails')
    formdata = {'form':form}
    return render(request, "createOrder.html", formdata)

@allowed_user(allowed_rules=['admin'])
def UpdateOrder(request,pk):
    updatedata = shop.objects.get(id=pk)
    form = OrderForm(instance=updatedata)

    if request.method == 'POST':
        form = OrderForm(request.POST,instance=updatedata)
        if form.is_valid():
            form.save()
            return redirect('ndetails')


    formdata = {'form':form}
    return render(request, "createOrder.html",formdata)
@allowed_user(allowed_rules=['admin'])
def remove(request,pk):
    deletedata = shop.objects.get(id=pk)
    if request.method == "POST":
        deletedata.delete()
        return redirect("ndetails")

    deleted = {'item':deletedata}
    return render(request, "remove.html",deleted)

def services(request):
    return render(request, "services.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactDisplay = Contact(name=name, email=email, subject=subject, message=message, date=datetime.today())
        ContactDisplay.save()

    return render(request, "contact.html")

@login_required(login_url="login")
@allowed_user(allowed_rules=['customer'])
def settings(request):
    customer = request.user.customer
    form = Customerform(instance=customer)

    if request.method == 'POST':
        form = Customerform(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, "settings.html", context)
