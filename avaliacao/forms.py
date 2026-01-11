from django import forms
from django.contrib.auth.models import User
from .models import Avaliacao, Nota, Colaborador

class CadastroUsuarioForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm password"
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {
            'username': '',
            'email': '',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem")
        return cleaned_data

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['avaliado', 'observacao']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['criterio', 'valor']
        widgets = {
            'valor': forms.NumberInput(attrs={
                'min': 0,
                'max': 10,
                'value': 0
            })
        }

class ColaboradorForm(forms.ModelForm):
    username = forms.CharField(label="Usuário")
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput
    )
    email = forms.EmailField(required=False)

    class Meta:
        model = Colaborador
        fields = ['nome', 'cargo', 'setor']