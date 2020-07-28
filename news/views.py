from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from news.serializers import CategoryListSerializer, ArticleListSerializer
from .models import Category, Article


class CategoryListViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategoryListSerializer


class ArticleFieldViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('id')
    serializer_class = ArticleListSerializer


@login_required
def article_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    articles = Article.objects.all()
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        articles = Article.objects.filter(category_id=category)
    return render(request,
                  'news/article/list.html',
                  {'category': category,
                   'categories': categories,
                   'articles': articles})


@login_required
def article_detail(request, id, slug):
    article = get_object_or_404(Article,
                                id=id,
                                slug=slug)
    return render(request,
                  'news/article/detail.html',
                  {'article': article})



