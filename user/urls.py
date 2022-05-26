from django.urls import path
from .views import Send_email, about, index, contact, kurs, narx, ustoz, yangilik

urlpatterns = [
    path('', index, name='index'),
    path('ustoz', ustoz, name='ustoz'),
    path('about', about, name='about'), 
    path('contact', contact, name='contact'),
    path('statistik', contact, name='statistik'),
    path('yangilik', yangilik, name='yangilik'),
    path('kurs', kurs, name='kurs'),
    path('narx', narx, name='narx'),
    path('tugma', Send_email, name='tugma'),
   
    
]