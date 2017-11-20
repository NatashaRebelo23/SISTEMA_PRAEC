from django.conf.urls import url
from django.contrib import admin
from . import views  

app_name = 'bolsistas_praec'
urlpatterns = [
	url(r'^index/$', views.index, name='index'),
    url(r'^registro/$', views.registrar_usuario, name='registrar_usuario'),  
    url(r'^addAluno/$', views.alunoCreateView.as_view(), name='add_aluno'),    
    url(r'^alunos/(?P<pk>\d+)$', views.aluno_detail.as_view(), name='aluno_detail'),
]
