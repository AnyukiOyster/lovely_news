from django.shortcuts import render
from .models import NewsCategory, News, random_news


# Create your views here.
#Главная страница
def home_page(request):
    #Достаём данные из БД
    news_list = News.objects.all()
    categories = NewsCategory.objects.all()
    nums = random_news()
    num1 = nums[0]
    num2 = nums[1]
    article1 = News.objects.get(id=num1)
    article2 = News.objects.get(id=num2)
    news_pool = []
    for a in news_list[::-1]:
        news_pool.append(a)

    #Передаём данные на FE
    context = {'news_list': news_list, 'categories': categories,'news_pool': news_pool, 'article1': article1, 'article2': article2}

    return render(request, 'home.html', context)

#Страница с новостями
def news_page(request, pk):
    #Вывод новости
    news = News.objects.get(id=pk)
    categories = NewsCategory.objects.all()
    #Передаём на фронтэнд
    context = {'news': news, 'categories': categories}

    return render(request, 'news_page.html', context)

#Страница категорий
def section_page(request, pk):
    category = NewsCategory.objects.get(id=pk)
    categories = NewsCategory.objects.all()
    news = News.objects.filter(news_category=category)[::-1]
    #Передаём на фронтэнд
    context = {'category': category, 'categories': categories, 'news': news}

    return render(request, 'section.html', context)