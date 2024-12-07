from django.db import models

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
    news_image = models.ImageField()
    news_image_subtext = models.CharField(max_length=512)
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.news_header)