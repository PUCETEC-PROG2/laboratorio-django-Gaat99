from django import forms 
from .models import Pokemon,Trainer


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__' 
        labels={
            'name':'Nombre',
            'type':'Tipo',
            'height':'Altura',
            'weight':'Peso',
            'trainer':'Entrenador',
            'picture':'Foto'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'  
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'weight': 'Peso',
            'level': 'Nivel',
            'birth': 'Fecha de Nacimiento',
            'picture': 'Foto',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el apellido'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso en kg'}),
            'level': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nivel de experiencia'}),
            'birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }