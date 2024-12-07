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

#Страница с новостями
def news_page(request, pk):
    #Вывод новости
    news = News.objects.get(id=pk)
    #Передаём на фронтэнд
    context = {'news': news}

    return render(request, 'news_page.html', context)

#Страница категорий
def section_page(request, pk):
    section = NewsCategory.objects.get(id=pk)
    news = News.objects.filter(news_category=section)
    #Передаём на фронтэнд
    context = {'section': section, 'news': news}

    return render(request, 'section.html', context)