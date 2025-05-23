from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a',
                'placeholder': "Escreva aqui",
            }
        ),
        help_text="Texto de ajuda para o seu usuário",
    )

    picture = forms.ImageField(
        widget=forms.FileField(
            attrs={
                'accept': 'image/*',
            }
        )
    )
    class Meta:
        model = models.Contact
        fields = (
            "first_name", "last_name", "phone",
            "email", "description", "category",
            "picture",

        )
    

    def clean(self):
        cleaned_data = self.cleaned_data
        print
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                "Primeiro nome não pode ser igual o segundo",
                code="invalid",
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self,):
        first_name = self.cleaned_data.get('first_name')

        if first_name == "ABC":
            self.add_error(
                'first_name',
                ValidationError(
                    'Não digite ABC neste campo',
                    code="invalid"
                ))
        return first_name
