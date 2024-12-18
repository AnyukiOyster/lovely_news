from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('news/<int:pk>', views.news_page),
    path('section/<int:pk>', views.section_page),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view),
    path('search', views.search),
    path('to-fav/<int:pk>', views.to_fav, name='to_fav'),
    path('not-fav/<int:pk>', views.not_fav),
    path('favorite', views.fav_page)
]