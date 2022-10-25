from email import message
from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
# 회원 가입 페이지 및 user 데이터 생성
def signup(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        signup_form = CustomUserCreationForm()

    context = {
        'signup_form': signup_form,
    }

    return render(request, 'accounts/signup.html', context)

# 회원 조회 페이지(프로필 페이지)
def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)

    context = {
        'user': user,
    }

    return render(request, 'accounts/detail.html', context)


# 로그인 페이지 및 user 로그인
def login(request):
    if request.user.is_authenticated:
        messages.info(request, '이미 가입한 상태입니다.')
        return redirect('articles:index')
    
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        login_form = AuthenticationForm()

    context = {
        'login_form': login_form,
    }

    return render(request, 'accounts/login.html', context)

# 로그아웃
@login_required
def logout(request):
    auth_logout(request)
    
    return redirect('articles:index')

# 팔로우 / 언팔로우 처리
@ require_POST
def follow(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user.is_authenticated:
        # 자기 자신이 아닌 사람을 팔로우한 경우
        if request.user != user:
            # 이미 user를 팔로우한 경우, 팔로우 취소
            if request.user.followings.filter(pk=user_pk).exists():
                request.user.followings.remove(user)
            # user를 팔로우 안한 경우, 팔로우
            else:
                request.user.followings.add(user)
        # 자기 자신을 팔로우한 경우
        else:
            messages.warning(request, '자기 자신은 팔로우할 수 없습니다.')
        
        return redirect('accounts:detail', user_pk)
    else:
        return redirect('accounts:login')

# 팔로잉 목록 페이지
def following(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)

    context = {
        'user': user,
    }

    return render(request, 'accounts/following.html', context)

# 팔로워 목록 페이지
def follower(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)

    context = {
        'user': user,
    }

    return render(request, 'accounts/follower.html', context)