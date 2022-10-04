from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
# 글 목록 페이지
def index(request):
    articles = Article.objects.all().order_by("-pk")

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


# 글 상세 페이지
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


# 글 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)

    article.delete()

    return redirect("articles:index")
