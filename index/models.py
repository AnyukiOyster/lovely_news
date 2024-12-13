from django.db import models
import random

# Список категорий новостей.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=64)
    category_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.category_name)

# Список самих новостей.
class News(models.Model):
    news_header = models.CharField(max_length=256)
    news_text = models.TextField()
    news_image = models.ImageField(upload_to='media')
    news_mini_image = models.ImageField(upload_to='media')
    news_image_subtext = models.CharField(max_length=512)
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.news_header)


# Генерация случайных новостей для главной
def random_news():
    news_all = News.objects.all()
    amount_news = int(len(news_all) +1)
    i = 1
    while i == 1:
        random_num1 = random.randrange(1, amount_news, 1)
        random_num2 = random.randrange(1, amount_news, 1)
        if random_num1 == random_num2:
            i = 1
        else:
            i = 0
            return random_num1, random_num2