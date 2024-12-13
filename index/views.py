from django.shortcuts import render, redirect
from .models import NewsCategory, News, random_news
from .forms import RegForm
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


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

class Register(View):
    template_name = 'registration/register.html'

    #Вывод формы регистрации
    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_name, context)

    #Получение информации от пользователя
    def post(self, request):
        form = RegForm(request.POST)

        #Проверка корректности данных
        if form.is_valid():
            username = form.clean_username()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            #Создание объекта класса User
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()

            #Авторизация пользователя
            login(request, user)
            return redirect('/')

        #Если данные некорректны
        context = {'form': RegForm, 'message': "Неверный адрес электронной почты или пароль"}
        return render(request, self.template_name, context)

# Поиск
def search(request):
    if request.method == 'POST':
        get_news = request.POST.get('search')

        if News.objects.get(news_header__iregex=get_news):
            searched_news = News.objects.get(news_header__iregex=get_news)
            return redirect(f'/news/{searched_news.id}')
        else:
            return redirect('/')