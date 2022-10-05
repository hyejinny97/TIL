from nntplib import ArticleInfo
from django.shortcuts import render, redirect

import articles
from .models import Article
from .forms import ArticleForm

# Create your views here.
# 루트페이지
def index(request):
    articles = Article.objects.all().order_by("-updated_at")

    context = {
        "articles": articles,
    }

    return render(request, "articles/index.html", context)


# 글 작성 페이지 및 데이터 생성
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
    elif request.method == "GET":
        form = ArticleForm()

    context = {
        "form": form,
    }

    return render(request, "articles/create.html", context)


# 상세글 페이지
def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        "article": article,
    }

    return render(request, "articles/detail.html", context)


# 글 수정 페이지 및 데이터 수정
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:detail", pk)
    elif request.method == "GET":
        form = ArticleForm(instance=article)

    context = {
        "form": form,
        "article": article,
    }

    return render(request, "articles/update.html", context)


# 데이터 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        article.delete()
        return redirect("articles:index")
    # else:
    #     context = {
    #         'error': True,
    #         'error_message': '삭제할 수 없습니다.'
    #     }
    #     return render(request, 'articles/index.html', context)
