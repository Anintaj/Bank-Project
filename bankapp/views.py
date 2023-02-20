from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from . models import account

from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render (request,"index.html")

def login(request):
    if request.method=='POST':
        username =request.POST['username']
        password =request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request, "Success.html")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")
def create(request):
    return render(request, "register.html")

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Try another Username")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save();
                print("User Created")
        else:
            messages.info(request, "Passwords not matching")
            return redirect('register')
        # return redirect('login')
        return render(request,"login.html")

    return render(request, "register.html")

def accform(request):
    return render(request, "accform.html")


def account_application(request):
    if request.method == 'POST':
        # Get the form data from the request
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        account_type = request.POST.get('account-type')
        materials_provided = request.POST.getlist('materials-provided')
        acc = account(name=name, dob=dob, age=age, gender=gender, phone=phone, email=email,
                          address=address, district=district, branch=branch, account_type=account_type,
                          materials_provided=','.join(materials_provided))
        acc.save()
        if not account.objects.filter (name=name).exists():

            messages.info(request,"Application Accepted")
        else:
            messages.info(request, "Application Accepted")
        # return redirect('account_application')

    return render(request, "accform.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

