from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('news/<int:pk>', views.news_page),
    path('section/<int:pk>', views.section_page)
]