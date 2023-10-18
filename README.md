# Atividade 8 - sexta-feira 13/10 (ponto facultativo)
**Aluno(a):Yasmin Carvalho Targino de Alencar**

## 1.Passo 1: Criar um novo app
Inicialmente, iremos criar um novo app, onde criaremos: o model, a view e o template da nossa aplicação. Neste exemplo o App se chamará tarefa, para cria-lo vamos usar o comando:

```bash
python manage.py startapp tarefa
```

## 2.Passo 2: Definindo um Modelo de Dados

Dentro do arquivo models.py no app iremos criar o modelo do dado que queremos listar. Basta criar a classe e colocar os campos com os respectivos tipos de dado, como no exemplo abaixo:

```python
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