from duvidas.models import *
from django import forms

class CadastroPerguntas(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(queryset=Pergunta.objects.all(), required=False)
    class Meta:
        model = Pergunta
        exclude = ('pergunta',)