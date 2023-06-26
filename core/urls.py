from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name="home"),
    path('logout', logout, name="logout"),
    path('registro', registro, name="registro"),
    path('carrito', carrito, name="carrito"),
    path('limpiar', limpiar),
    path('comprar', comprar, name="comprar"),
    path('addtocar/<codigo>', addtocar, name="addtocar"),
    path('dropitem/<codigo>', dropitem, name="dropitem"),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
]
