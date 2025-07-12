from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Categories,Product,SubCategories
from django.utils import timezone

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
            return redirect('index')
        else:
            return redirect('userlogin')

    return render(request,"swapshop/register.html")


def userlogout(request):
    logout(request)
    return redirect('index')

def dashboard(request):
    return render(request,'swapshop/dashboard.html')

def item(request):
    return render(request,'swapshop/item.html')

def addProduct(request):
    categories = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    return render(request,'swapshop/add-product.html',{'categories': categories,'subcategories': subcategories})



def addIteam(request):
    if request.method == 'POST':  
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES.get('image') 
        categary_id = request.POST.get('categary')
        subCategary_id = request.POST.get('subCategary')
        categary = Categories.objects.get(id=categary_id)
        subCategary = SubCategories.objects.get(id=subCategary_id)

        Product.objects.create(
            name=name,
            price=price,
            desc=desc,
            image=image,
            pub_date=timezone.now(),
            categary=categary,
            subCategary=subCategary,
            is_available=True,
            report_count=0
        )

        return redirect('dashboard')

        

    categories = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    return render(request, 'swapshop/add-product.html', {
        'categories': categories,
        'subcategories': subcategories
    })

    