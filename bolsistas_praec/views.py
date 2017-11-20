from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Siape,Usuario,Aluno
# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .forms import *
from django.views import generic

@login_required
def index(request):
    
    my_object = Siape.objects.filter(siape = request.user.usuario.siape)
    if my_object.count() == 0:
        return HttpResponse ("O SIAPE não é válido!")
    return render(request, 'bolsistas_praec/praec.html', {})


class alunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm

class aluno_detail(generic.DetailView):
    model = Aluno
    
def registrar_usuario(request):
#    if request.user.is.authenticated:
#       return redirect('bolsistas_praec: ')
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        usuario_form = UsuarioForm(data=request.POST)
        if user_form.is_valid() and usuario_form.is_valid():
            user = user_form.save(commit=False)
            usuario = usuario_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            usuario.usuario = user
            usuario.save()
            return redirect('/accounts/login')
        else:
            user_form = UserForm()
            usuario_form = UsuarioForm()
        return render(request, 'bolsistas_praec/templates/registration/login.html',
                      {'user_form': user_form,
                       'usuario_form': usuario_form})
    