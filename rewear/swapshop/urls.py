from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('login/',views.userlogin,name="userlogin"),
    path('singup/',views.usersingup,name="usersingup"),
    path('logout/',views.userlogout,name="userlogout"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('add-product/',views.addProduct,name="addProduct"),
    path('addIteam/',views.addIteam,name="addIteam"),
]
