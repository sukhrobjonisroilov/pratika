from django.contrib import admin
from .models import TelecomAdmin,TelecomUser
# Register your models here.
@admin.register(TelecomAdmin)
class TelecomAdmin(admin.ModelAdmin):
    list_display = ['ism','familiya','mahalla']
    search_fields = ('ism', 'familiya','ochistiva')

@admin.register(TelecomUser)
class TelecomUserAdmin(admin.ModelAdmin):
    list_display = ['router_name']
    search_fields = ['router_name']