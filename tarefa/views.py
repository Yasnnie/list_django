from django.shortcuts import render
from .models import Task

# Create your views here.

def listar_produtos(request):
    tasks = Task.objects.all()
    return render(request, 'lista_tarefas.html', {'tasks': tasks})