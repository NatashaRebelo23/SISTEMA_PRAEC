from django import forms
from .models import *
from django.contrib.auth.models import User
from django.conf import settings

class UserForm(forms.ModelForm):
    password = forms.CharField(
        required = True,
        label = 'Senha',
        max_length = 32,
        min_length = 8,
        widget = forms.PasswordInput()
    )
    username = forms.CharField(
        required = True,
        label = 'Nome do usuário',
        max_length = 150,
        help_text = ""
    )
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Nome de usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'password': 'Senha',
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('siape',)
        labels = {
            'siape': 'Código SIAPE',
            }

class AlunoForm(forms.ModelForm):
    data_preenchimento = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    data_preenchimento_termino = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Aluno
        fields = '__all__'
        labels = {
	    'nome': 'Nome do aluno',
	    'matricula': 'Matricula do aluno',
	    'curso': 'Curso do aluno',
	    'periodo': 'Periodo do aluno no curso',
	    'renda_familiar': 'Renda familiar do aluno',
	    'cpf': 'CPF do aluno',
	    'data_preenchimento': 'Data de Preenchimento do cadastro',
        'data_preenchimento_termino': 'Data de Término do cadastro',
	}

class Bolsa_AuxilioForm(forms.ModelForm):
    #pesquisa o aluno e vincula a bolsa
    class Meta:
        model = Bolsa_Auxilio
        fields = ('tipo',)
        labels = {
            'tipo': 'Tipo de Bolsa Auxílio',
        }

class Bolsa_Remunerada_400Form(forms.ModelForm):
    class Meta:
        model = Bolsa_Remunerada_400
        fields = ('tipo',)
        labels = {
             'tipo': 'Tipo de Bolsa Remunerada',
        }
