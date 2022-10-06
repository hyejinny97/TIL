from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
# 영화 정보 목록 페이지
def index(request):
    movies = Movie.objects.all()

    context = {
        'movies': movies,
    }

    return render(request, 'movies/index.html', context)

# 영화 정보 상세 페이지
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }

    return render(request, 'movies/detail.html', context)

# 영화 정보 등록 페이지 및 데이터 생성
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie1 = form.save(commit=False)
            movie1.imgfile = request.FILES.get('imgfile')
            movie1.save()
            return redirect('movies:detail', movie1.pk)
    elif request.method == 'GET':
        form = MovieForm()
    
    context = {
        'form': form,
    }

    return render(request, 'movies/create.html', context)

# 영화 정보 수정 페이지 및 데이터 수정
# 참고: https://bamgorae.tistory.com/59
def update(request, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie1 = form.save(commit=False)
            movie1.imgfile = request.FILES.get('imgfile')
            movie1.save()
            return redirect('movies:detail', movie.pk)
    elif request.method == 'GET':
        form = MovieForm(instance=movie)

    context = {
        'form': form,
        'movie': movie,
    }

    return render(request, 'movies/update.html', context)

# 영화 정보 삭제
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')