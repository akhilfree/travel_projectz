from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import Place,Team

# Create your views here.

def home(request):
    obj=Place.objects.all()
    obj1 = Team.objects.all()


    return render(request,'index.html',{'result':obj,'result1':obj1})




def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalied details')
            return redirect('login')

    return render(request,'login.html')




def register1(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register1')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('register1')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                        first_name=first_name, last_name=last_name)
                user.save();
                return redirect('login')
                # print('user is created')
        else:
            print('password is not matching')
            return redirect('/')


    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')










    

