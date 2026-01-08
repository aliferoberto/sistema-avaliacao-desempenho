from django import forms
from .models import Avaliacao, Nota

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['avaliado', 'observacao']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['criterio', 'valor']