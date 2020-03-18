from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# from mapapp.models import latlng

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
               user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
               user.save();
               return redirect("login")
        else:
            messages.info(request,'password doest match')
            return redirect('register')
    else:
        return render(request,'registration.html')





def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=auth.authenticate(request, username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("map")
        else:
            messages.info(request,'not registered')
            return redirect('login')
    else:
        return render(request,'login.html')

        
def map(request):
    if request.method == 'POST':
        latitude=request.POST.get('latitude')
        longitude=request.POST.get('longitude')
        pos=latlng(latitude=latitude,longitude=longitude)
        pos.save();
        return redirect("map")
    return render(request,'map.html')
    
