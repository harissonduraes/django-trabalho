from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'usuarios/index.html', {})

def w3c(request):
    return render(request, 'usuarios/w3c.html')

def html(request):
    return render(request, 'usuarios/html.html')

def contato(request):
    form = ContatoForm(request.POST or None)
    context={
        'form':form
       
    }
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem Enviada')
            messages.success(request, 'E-mail enviado com sucesso')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')
            form = ContatoForm()

        else:
            messages.error(request,'Erro ao enviar e-mail')
    return render(request, 'usuarios/contato.html', context)