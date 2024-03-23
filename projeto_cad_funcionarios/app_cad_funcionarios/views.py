from django.shortcuts import render
from .models import Funcionario

def home(request):
    return render(request, 'usuarios/home.html')

def funcionarios(request):
    novo_funcionario = Funcionario()
    novo_funcionario.nome = request.POST.get('nome')
    novo_funcionario.cargo = request.POST.get('cargo')
    novo_funcionario.save()

    # Exibindo todos os funcionarios cadastrados

    funcionarios = {
        'funcionarios': Funcionario.objects.all()
    }

    # Retornar os dados para a pagina de listagem

    return render(request, 'usuarios/funcionarios.html', funcionarios)