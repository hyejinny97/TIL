from django.shortcuts import render

# Create your views here.
# 메인페이지
def index(request):
    return render(request, 'home/index.html')