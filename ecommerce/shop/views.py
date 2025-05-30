from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.


def home(request):
    products=Products.objects.all()
    return render(request,'index.html',{'products':products})

def about(request):
    return render(request,'about.html',{})

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,"You have logged in")
            return redirect ('home')
        else:
            messages.error(request,'Wrong Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request,"Logged Out")
    return redirect('home')

def register(request):
    form=SignUpForm()
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request,"Something went Wrong... Try again..!")
            return redirect('register')
    else:
        return render(request,'register.html',{'form':form})
    

def product(request,pk):
    product=Products.objects.get(id=pk)

    return render(request,'product.html',{'product':product})

def category(request):
    return render(request,'category.html',{})