from django.conf.urls import url

from apps.usuario.views import index, RegistroUsuario

urlpatterns = [
    url(r'^$', index),
    url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),

]
