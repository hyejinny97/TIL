from django.shortcuts import render, redirect
from .models import Articles

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    context = {
        "articles": articles,
    }

    return render(request, "app2/index.html", context)


def create(request):
    content = request.GET.get("article")
    Articles.objects.create(content=content)

    return redirect("/app2/")
