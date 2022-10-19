from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

# Create your views here.
# 게시글 목록 페이지
def index(request):
    articles = Article.objects.order_by('-updated_at')

    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)

# 게시글 작성 페이지 및 게시글 데이터 생성
@require_http_methods(["GET", "POST"])
@login_required
def article_create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.writer = request.user
            article.save()
            messages.info(request, '해당 글을 생성했습니다.')
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()

    context = {
        'article_form': article_form,
    }

    return render(request, 'articles/create.html', context)

# 게시글 상세 페이지
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()

    context = {
        'article': article,
        'comment_form': comment_form,
    }

    return render(request, 'articles/detail.html', context)

# 게시글 수정 페이지 및 게시글 데이터 수정
@require_http_methods(["GET", "POST"])
@login_required
def article_update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.writer:  
        if request.method == 'POST':
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                article = article_form.save()
                messages.success(request, '해당 게시글을 수정했습니다.')
                return redirect('articles:detail', article_pk)
        else:
            article_form = ArticleForm(instance=article)

        context = {
            'article': article,
            'article_form': article_form,
        }

        return render(request, 'articles/update.html', context)
    else:
        messages.warning(request, '수정 권한이 없습니다.')
        return redirect('articles:index')

# 게시글 삭제
# @require_http_methods(["POST"])
@login_required
def article_delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.writer:  
        article.delete()
        return redirect('articles:index')
    else:
        messages.warning(request, '삭제 권한이 없습니다.')
        return redirect('articles:index')

# 댓글 데이터 생성
@require_http_methods(["POST"])
@login_required
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.writer = request.user
        comment.save()
    else:
        messages.error(request, '댓글 형식이 올바르지 않습니다.')
    
    return redirect('articles:detail', article_pk)

# 댓글 데이터 삭제
# @require_http_methods(["POST"])
@login_required
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.writer:
        comment.delete()
    else:
        messages.warning(request, '삭제 권한이 없습니다.')

    return redirect('articles:detail', article_pk)