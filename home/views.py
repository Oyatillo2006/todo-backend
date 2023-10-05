from django.shortcuts import render, redirect
from .models import Todo

def home(request):
    if request.POST:
        title = request.POST.get("title")
        time = request.POST.get("time")
        docs = request.POST.get("docs")
        status = request.POST.get("status")


        Todo.objects.create(title = title, time = time, docs = docs, status =status)
        return redirect("/")

    context = {
        "todos": Todo.objects.all()
    }
    return render(request, "todo.html", context)

def delete(request, id):
    Todo.objects.get(id=id).delete()
    return redirect("/")

def todo_edit(request, id):
    if request.POST:
        title = request.POST.get("title")
        time = request.POST.get("time")
        docs = request.POST.get("docs")
        status = request.POST.get("status")

        Todo.objects.filter(id=id).update(title = title, time = time,docs = docs, status = status)
        return redirect("/")

    context = {
        "todo": Todo.objects.get(id=id)
    }
    return render(request,"todo_edit.html", context)

