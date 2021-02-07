
from .views import Home,Signup,Login,logout,Cart,Checkout,OrderView 
from .auth import LoginCheckMiddleware,LogoutCheckMiddleware
from django.urls import path,include
from django.contrib.auth import views as as_view
from . import views



urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('logout',LoginCheckMiddleware(logout), name='logout'),
    path('cart',Cart.as_view(), name='cart'),
    path('signup',LogoutCheckMiddleware(Signup.as_view()), name='signup'),
    path('login',LogoutCheckMiddleware(Login.as_view()), name='login'),
    path('checkout',LoginCheckMiddleware(Checkout.as_view()), name='checkout'),
    path('order',LoginCheckMiddleware(OrderView.as_view()), name='order'),
]