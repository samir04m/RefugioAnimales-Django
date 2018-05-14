from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from apps.usuario.forms import RegistroForm

def index(request):
	return HttpResponse('usuario/index.html')

class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('mascota:mascota_listar')
