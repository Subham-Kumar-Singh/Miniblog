from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('about/', views.About, name="about"),
    path('contact/', views.Contact, name='contact'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('login/', views.Loginfunc, name="login"),
    path('singup/', views.Signupfunc, name="signup"),
    path('logout/', views.Logoutfunc, name="logout"),
]
