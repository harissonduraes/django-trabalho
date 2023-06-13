from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

def send_mail(self):
    nome = self.cleaned_data['nome']
    email = self.cleaned_data['email']
    assunto = self.cleaned_data['assunto']
    mensagem = self.cleaned_data['mensagem']

    conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem:{mensagem}'
    mail = EmailMessage (
    subject='E-mail enviado pelo sistema Django',
    body=conteudo,
    from_email='contato@seudominio.com.br',
    to=['contato@seudominio.com.br', ],
    headers={'Reply.To':email},
    )
    mail.send()