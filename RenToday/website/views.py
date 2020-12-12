from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from website.models import Property

# Create your views here.

def index(request):

    pop_dest = [
        {'name': 'Lonavala',
        'no': '10 villas',
        'img': 'pics/1.png'},

        {'name': 'Igatpuri',
        'no': '6 villas',
        'img': 'pics/2.png'},
    ]

    data = {'pop_dest': pop_dest}

    return render(request, "index.html", data)

def properties(request):
    props = Property.objects.all()
    return render(request, "properties.html", {'props': props})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']
        email = request.POST['email']

        if psw == psw_repeat:
            user = User.objects.create_user(username=username,password=psw,first_name=first_name,last_name=last_name,email=email)
            return render(request, "login.html")
        else:
            return render(request, "register.html")



    else:
        return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'Invalid credentials')
            return render(request, "login.html")


    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

     
