from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('login/',views.userlogin,name="userlogin"),
    path('singup/',views.usersingup,name="usersingup"),
    path('logout/',views.userlogout,name="userlogout"),

]
