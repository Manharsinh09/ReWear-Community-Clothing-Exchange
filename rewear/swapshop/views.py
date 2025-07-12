from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'swapshop/index.html')

def usersingup(request):
    if request.method=='POST':
        
        first_name = request.POST.get('Firstname')
        last_name = request.POST.get('Lastname')
        uname = request.POST.get('Username')
        upass = request.POST.get('Password')
        email = request.POST.get('Email')
        print(uname,upass,email)

        new_user = User.objects.create_user(uname,email,upass)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        
    return render(request,"swapshop/register.html")

def userlogin(request):
    if request.method=='POST':
        username = request.POST.get('Username')
        upass1 = request.POST.get('Password')
        
        user = authenticate(request,username=username,password=upass1)
        if user is not None:
            login(request,user)
            return redirect('shop')
        else:
            return redirect('userlogin')

    return render(request,"swapshop/register.html")


def userlogout(request):
    logout(request)
    return redirect('shop')
