from django.shortcuts import render
from .models import NewsCategory, News

# Create your views here.
#Главная страница
def home_page(request):
    #Достаём данные из БД
    news_list = News.objects.all()
    categories = NewsCategory.objects.all()
    #Передаём данные на FE
    context = {'news_list': news_list, 'categories': categories}

    return render(request, 'home.html', context)