
from django.contrib import admin
from django.urls import path

from TravelApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='price'),
    path('services/', views.services, name='services'),
    path('', views.register, name='register'),
    path('Login/', views.login, name='login'),
    path('basic/', views.basic, name='basic'),
    path('premium/', views.premium, name='premium'),
    path('plus/', views.plus, name='plus'),
    path('book/', views.book, name='book'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),



]
