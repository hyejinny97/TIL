from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm

# Create your views here.
# 회원 목록 페이지
def index(request):
    users = get_user_model().objects.all()

    context = {
        'users': users,
    }

    return render(request, 'accounts/index.html', context)

# 회원 가입 페이지 및 유저 데이터 생성
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    elif request.method == 'GET':
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    
    return render(request, 'accounts/signup.html', context)

# 회원 정보 상세 페이지(프로필 페이지)
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)

    context = {
        'user': user,
    }

    return render(request, 'accounts/detail.html', context)

# 로그인 페이지 및 로그인 처리
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    elif request.method == 'GET':
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)

# 로그아웃 처리
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')