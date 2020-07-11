from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Category, Article
from .forms import ArticleForm



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


@login_required
def manage_articles(request):
    user_id = request.user.id
    articles = Article.object.filter(user_id=user_id)
    return render(request,
                    'news/article/manage.html',
                    {'articles':articles})


@login_required
def edit_article(request, id, slug):
    if request.method == 'POST':
        article_form = ArticleForm(
                                instance=get_object_or_404(Article, 
                                                        id=id, slug=slug),
                                 data=request.POST)
        if article_form.is_valid():
            article_form.save()

            messages.success(request, 'Profile updated '\
                                        'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = ArticleForm(instance=request.user)

    return render(request,
                  'account/edit.html',
                  {'user_form': user_form})

