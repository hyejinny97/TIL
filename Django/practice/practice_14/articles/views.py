from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
# 게시글 목록 조회 페이지
def index(request):
    articles = Article.objects.order_by('-updated_at')

    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)

   

# 게시글 데이터 생성
@login_required
def article_create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.writer = request.user
            article.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    
    context = {
        'article_form': article_form,
    }

    return render(request, 'articles/article_create.html', context)
    
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
@login_required
def article_update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.writer:
        if request.method == 'POST':
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                article_form.save()
                return redirect('articles:detail', article.pk)
        else:
            article_form = ArticleForm(instance=article)

        context = {
            'article': article,
            'article_form': article_form,
        }

        return render(request, 'articles/article_update.html', context)
    else:
        return redirect('articles:detail', article.pk)

# 게시글 삭제
@login_required
def article_delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.writer:
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

# 게시글 좋아요
@login_required
def article_like(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # 로그인한 사용자가 이미 해당 글에 좋아요를 누른 경우
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    
    return redirect('articles:detail', article_pk)

# 댓글 데이터 생성
@login_required
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.writer = request.user
        comment.article = article
        comment.save()
    
    return redirect('articles:detail', article.pk)
    
# 댓글 데이터 삭제
@login_required
def comment_delete(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.writer:
        comment.delete()
    
    return redirect('articles:detail', article.pk)

# 댓글 좋아요
@login_required
def comment_like(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)
    # if request.user in comment.like_users.all():
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    
    return redirect('articles:detail', article_pk)