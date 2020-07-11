from django.urls import path
from news import views

urlpatterns = [
     path('', views.article_list, name='article_list'),
     path('<slug:category_slug>/', views.article_list,
          name='article_list_by_category'),
     path('<int:id>/<slug:slug>/', views.article_detail,
          name='article_detail'),


]