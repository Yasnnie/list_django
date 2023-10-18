from django.shortcuts import render
from .models import Task

def listar_produtos(request):
    tasks = Task.objects.all()
    return render(request, 'lista_tarefas.html', {'tasks': tasks})