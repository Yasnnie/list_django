# Atividade 8 - sexta-feira 13/10 (ponto facultativo)
**Aluno(a):Yasmin Carvalho Targino de Alencar**

## Passo 1: Criar um novo app
Inicialmente, iremos criar um novo app, onde criaremos: o model, a view e o template da nossa aplicação. Neste exemplo o App se chamará tarefa, para cria-lo vamos usar o comando:

```bash
python manage.py startapp tarefa
```

Além disso, precisamos cirar dentro do nosso app um arquivo chamado `urls.py` onde vamos definir as rotas referentes aquele app. Nesse caso iremos apontar para a view que irá controlar a nossa listagem.

```python
from django.urls import path
from . import views

urlpatterns = [
   path('', views.listar_produtos, name="index")
]
```

Por fim, devemos adiciorar as urls do app a aplicação geral:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', include('tarefa.urls')),
]
```

## Passo 2: Definir um Modelo de Dados

Dentro do arquivo `models.py` no app iremos criar o modelo do dado que queremos listar. Basta criar a classe e colocar os campos com os respectivos tipos de dado, como no exemplo abaixo:

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    descricao = models.TextField()
```

Em seguida devemos rodar as migrations para atualizar o nosso banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

Para inserir novos dados, devemos criar um super user para acessar o admin. Lá iremos cadastrar as tarefas para serem listadas.

```bash
python manage.py createsuperuser
```

## Passo 3: Criar uma View

Iremos criar uma classe dentro do arquivo `views.py` do app para manipular os dados do model e controlar o template. Como no exemplo:

```python
from django.shortcuts import render
from .models import Task

def listar_produtos(request):
    tasks = Task.objects.all()
    return render(request, 'lista_tarefas.html', {'tasks': tasks})
```

## Passo 4: Criar um template

Para o último passo vamos criar uma pasta chamada templates, nela adicionaremos nossos arquivos html, nesse caso iremos criar o `lista_tarefas.html`. Para fazer a listagem dos dados nesse arquivo vamos criar uma uma `<ul>` e dentro dela vamos abrir o for que criará as `<li>` da nossa lista e passará as informações de cada objeto que virá da view.


```html
  <ul>
        {% for t in tasks %}
        <li>
            <h3>{{ t.title }} - {{ t.data }}</h3>
            <p>{{t.descricao}}</p>
        </li>
        {% endfor %}
    </ul>
```

## Referências:
1. https://docs.djangoproject.com/en/4.2/
2. https://www.youtube.com/watch?v=DNGI5aD9MJs