from django.shortcuts import render
from news.models import NewsContent
# Create your views here.

def homeView(response):
    news = NewsContent.objects.filter().order_by('-pk')[:3]
    return render(response, 'home.html', {'news': news})