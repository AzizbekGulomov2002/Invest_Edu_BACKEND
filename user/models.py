from distutils.command.upload import upload
from email.policy import default
from tabnanny import verbose
from django.db import models



class Menyu_Fanlar(models.Model):
    rasm = models.ImageField(upload_to='rasmlar/%Y/%m/%d',null=True)
    fan_nomi = models.CharField(max_length=100)
    fan_haqida = models.CharField(max_length=130)
    
    
    def __str__(self):
        return self.fan_nomi + ' ' + self.fan_haqida
    
    class Meta:
        verbose_name = 'Fan Menyusi'    
        verbose_name_plural = 'Fanlar Menyusi'    
        
        
class Statistika(models.Model):
    ijtimoiy_tarmoq = models.IntegerField()
    oquvchilar_soni = models.IntegerField()
    kontentlar_soni = models.IntegerField()
    ustozlar_soni = models.IntegerField()
    
    def __str__(self):
        return str(self.ijtimoiy_tarmoq) + ' ' + str(self.oquvchilar_soni) + ' ' + str(self.kontentlar_soni) + ' ' + str(self.ustozlar_soni)
    
    class Meta:
        verbose_name = 'Statistika'
        verbose_name_plural='Statistikalar'
        
        
class Bizning_faxrimiz(models.Model):
    rasm = models.ImageField(upload_to='rasmlar/%Y/%m/%d',null=True)
    ism_sharif = models.CharField(max_length=100)
    malumot = models.CharField(max_length=240, null=True, blank=True)
    
    def __str__(self):
        return self.ism_sharif + ' ' + self.malumot
    
    class Meta:
        verbose_name = 'Bizning faxrimiz'
        verbose_name_plural = 'Bizning faxrimiz'
        
    
class Oqituvchilar(models.Model):
    rasm = models.ImageField(upload_to='rasmlar/%Y/%m/%d',null=True)
    ism_sharif = models.CharField(max_length=100)
    vazifasi = models.CharField(max_length=500)
    
    def __str__(self):
        return self.ism_sharif + ' ' + self.vazifasi
    
    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"
        
        
class Yangiliklar(models.Model):
    rasm =  models.ImageField(upload_to='rasmlar/%Y/%m/%d',null=True)
    sarlavha = models.CharField(max_length=100)
    vaqt = models.DateField(auto_now_add=True)
    malumot = models.TextField()
    kurishlar = models.IntegerField(default=1)
    
    def __str__(self):
        return self.sarlavha + ' ' + self.malumot + "" + str(self.kurishlar)
    
    
    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'yangiliklar'
        
        
class Kurs_narxlar(models.Model):
    kurs_nomi = models.CharField(max_length=100)
    kurs_narxi = models.IntegerField()
    kurs_haqida = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.kurs_nomi + ' ' + str(self.kurs_narxi) + ' ' + self.kurs_haqida
    
    class Meta:
        verbose_name = 'Kurs narxi'
        verbose_name_plural = 'Kurs narxlari'
    
    
    
    
    
    
    
    
