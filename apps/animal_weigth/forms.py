from django import forms
from .models import AnimalWeigthModel


class AnimalWeigthForm(forms.ModelForm):

    # model = AnimalWeigthModel

    class Meta:
        model = AnimalWeigthModel
        fields = ['type_animal', 'weigth', 'earring_number']
