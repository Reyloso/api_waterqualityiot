from datetime import datetime

from django import forms
from django.forms import ModelForm

from configurations.models import Country

class CountryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Country
        fields = ['name', 'status',]
        labels = {
            'name': 'Nombre',
            'status': 'Estado'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            )
        }        

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data