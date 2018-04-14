from django import forms

from apps.adopcion.models import Persona, Solicitud

class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona

		fields = [
			'nombre',
			'apellidos',
			'edad',
			'telefono',
			'email',
			'domicilio',
		]
		labels = {
			'nombre': 'Nombre',
			'apellidos': 'Apellidos',
			'edad': 'Edad',
			'telefono': 'Telefono',
			'email': 'Correo electronico',
			'domicilio': 'Direccion Domicilio',
		}
		widgets = {
			'nombre': forms.TextInput(),
			'apellidos': forms.TextInput(),
			'edad': forms.NumberInput(),
			'telefono': forms.NumberInput(),
			'email': forms.EmailInput(),
			'domicilio': forms.Textarea(attrs={'rows': '1', 'class':'materialize-textarea'}),
		}


class SolicitudForm(forms.ModelForm):

	class Meta :
		model = Solicitud

		fields = [
			'numero_mascota',
			'razones',
		]
		labels = {
			'numero_mascota': 'Numero de Mascotas',
			'razones': 'Razones para adoptar',
		}
		widgets = {
			'numero_mascota': forms.NumberInput(),
			'razones': forms.Textarea(attrs={'rows': '5', 'class':'materialize-textarea'}),
		}