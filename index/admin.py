from django.contrib import admin
from .models import NewsCategory, News, Favorites

# Register your models here.
admin.site.register(NewsCategory)
admin.site.register(News)
admin.site.register(Favorites)