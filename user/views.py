
import smtplib
from tkinter.font import families
from django.shortcuts import redirect, render

from django.views import View
from .models import Menyu_Fanlar,Bizning_faxrimiz,Oqituvchilar,Statistika,Kurs_narxlar,Yangiliklar
from django.core.mail import send_mail
def index(request):
    context = {
        'menyu_fan' : Menyu_Fanlar.objects.all(),
        'statistik' : Statistika.objects.all(),
        'faxr_menu' : Bizning_faxrimiz.objects.all(),
        'ustoz' : Oqituvchilar.objects.all(),
        'yangilik':Yangiliklar.objects.all(),
        'kurs':Kurs_narxlar.objects.all()
    }
    
    return render(request,'basic/index.html',context) 
    
    


def yangilik(request):
    context = {
        'yangilik':Yangiliklar.objects.all(),
    }
    news=Yangiliklar.objects.get()
    news.kurishlar=news.kurishlar+1
    news.save()
    return render(request,'basic/blog.html',context)



def ustoz(request):
    context = {
        'ustoz' : Oqituvchilar.objects.all(),
    }
    return render(request, 'basic/teacher.html',context)



def kurs(request):
    context = {       
        'menyu_fan':Menyu_Fanlar.objects.all()
    }
    return render(request, 'basic/courses.html', context)
    
    
    
def about(request):
    return render(request,'basic/about.html') 

def contact(request):
    return render(request, 'basic/contact.html')

def narx(request):
    context = {
        'kurs':Kurs_narxlar.objects.all()
    }
    return render(request, 'basic/pricing.html', context)




