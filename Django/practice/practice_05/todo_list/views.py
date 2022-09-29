from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by("id")

    context = {
        "todos": todos,
    }

    return render(request, "todo/index.html", context)


# 할 일 추가
def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    todo = Todo(content=content, priority=priority, deadline=deadline)
    todo.save()

    return redirect("todo:index")


# 상태 변경
def update(request, id):
    todo = Todo.objects.get(id=id)

    if todo.completed == False:
        todo.completed = True
    else:
        todo.completed = False
    todo.save()

    return redirect("todo:index")


# 메모 삭제
def delete(request, id):
    todo = Todo.objects.get(id=id)

    todo.delete()

    return redirect("todo:index")
