from django import forms

from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota

		fields = [
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_rescate',
			'persona',
			'vacuna',
		]

		labels = {
			'nombre': 'Nombre',
			'sexo': 'Sexo',
			'edad_aproximada': 'Edad Aproximada',
			'fecha_rescate': 'Fecha de rescate', 
			'persona': 'Adoptante',
			'vacuna': 'Vacunas',
		}

		widgets = {
			'nombre': forms.TextInput(),
			'sexo': forms.TextInput(),
			'edad_aproximada': forms.TextInput(),
			'fecha_rescate': forms.TextInput(), 
			'persona': forms.Select(),
			'vacuna': forms.SelectMultiple(),
		}
