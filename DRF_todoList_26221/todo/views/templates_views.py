from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from ..models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = "todo/list.html"
    context_object_name = "todos"
    ordering = ["-created_at"]


class TodoCreateView(CreateView):
    model = Todo
    fields = ["name", "description", "complete", "exp"]
    template_name = "todo/create.html"
    success_url = reverse_lazy("todo:list")


class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo/detail.html"
    context_object_name = "todo"


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["name", "description", "complete", "exp"]
    template_name = "todo/update.html"
    context_object_name = "todo"
    success_url = reverse_lazy("todo:list")
