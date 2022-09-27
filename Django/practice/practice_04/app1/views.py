from django.shortcuts import render, redirect

articles = []

# Create your views here.
def index(request):
    context = {
        "articles": articles,
    }
    return render(request, "app1/index.html", context)


def create(request):
    article = request.GET.get("article")
    articles.append(article)

    return redirect("/app1/")
