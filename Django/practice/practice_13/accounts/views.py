from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .foms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.
# 회원 목록 페이지
@login_required
def index(request):
    if request.user.is_superuser:
        users = get_user_model().objects.all()

        context = {
            'users': users,
        }

        return render(request, 'accounts/index.html', context)
    else:
        messages.warning(request, '접근 권한이 없습니다.')
        return redirect('articles:index')

# 회원 프로필 페이지
@login_required
def detail(request, user_pk):
    if request.user.pk == user_pk or request.user.is_superuser:
        user = get_user_model().objects.get(pk=user_pk)
        
        context = {
            'user': user,
        }

        return render(request, 'accounts/detail.html', context)
    else:
        messages.warning(request, '접근 권한이 없습니다.')
        return redirect('articles:index')
        # return HttpResponseForbidden()

# 회원가입 페이지 및 user 데이터 생성
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

# 회원정보 수정 페이지 및 user 기본 정보(비밀번호 제외) 수정
@login_required
def update(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, '회원 정보를 수정했습니다.')
            return redirect('accounts:detail', request.user.pk)
    else:
        user_form = CustomUserChangeForm(instance=request.user)

    context = {
        'user_form': user_form,
    }

    return render(request, 'accounts/update.html', context)

# 비밀번호 변경 페이지 및 user 비밀번호 변경
@login_required
def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, '비밀번호를 변경했습니다.')
            return redirect('accounts:detail', request.user.pk)
    else:
        password_form = PasswordChangeForm(request.user)

    context = {
        'password_form': password_form,
    }

    return render(request, 'accounts/password.html', context)

# 회원 탈퇴
@login_required
def delete(request):
    request.user.delete()
    messages.warning(request, '회원 계정을 삭제했습니다.')
    
    return redirect('articles:index')

# 로그인
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form = AuthenticationForm(request, request.POST)
            if login_form.is_valid():
                auth_login(request, login_form.get_user())
                return redirect('articles:index')
        else:
            login_form = AuthenticationForm()

        context = {
            'login_form': login_form,
        }

        return render(request, 'accounts/login.html', context)
    else:
        messages.warning(request, '이미 로그인한 상태입니다.')
        return redirect('articles:index')

# 로그아웃
@login_required
def logout(request):
    auth_logout(request)

    return redirect('articles:index')
