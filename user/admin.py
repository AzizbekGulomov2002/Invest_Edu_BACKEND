from django.contrib import admin

from .models import Bizning_faxrimiz,Kurs_narxlar,Menyu_Fanlar,Oqituvchilar,Statistika,Yangiliklar

class Menyu_fanAdmin(admin.ModelAdmin):
    list_display = ['fan_nomi','fan_haqida']
    
admin.site.register(Menyu_Fanlar, Menyu_fanAdmin)


class StatistikAdmin(admin.ModelAdmin):
    list_display = ['ijtimoiy_tarmoq','oquvchilar_soni','kontentlar_soni','ustozlar_soni']
    
admin.site.register(Statistika, StatistikAdmin)

class OqituvchiAdmin(admin.ModelAdmin):
    list_display = ['ism_sharif','vazifasi']
admin.site.register(Oqituvchilar, OqituvchiAdmin)


admin.site.register(Bizning_faxrimiz)

class KursNarxAdmin(admin.ModelAdmin):
    list_display = ['kurs_nomi','kurs_narxi','kurs_haqida']
    
    
admin.site.register(Kurs_narxlar, KursNarxAdmin)
admin.site.register(Yangiliklar)