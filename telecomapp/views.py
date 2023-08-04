from django.shortcuts import render

# Create your views here.
from .models import TelecomAdmin,TelecomUser


def index_page(reuquests):
    news = TelecomUser.objects.all().order_by('-router_name')
    ctx ={
        'news':news
    }

    return   render(reuquests,'dependents.html',ctx)