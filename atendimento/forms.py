from django.forms import ModelForm, TextInput, DateInput, Select, NumberInput, EmailInput, Select
from . models import Cliente, Medico

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control'}),
            'dt_nasc': DateInput(attrs={'class':'form-control'}),
            'cpf': TextInput(attrs={'class':'form-control'}),
            'sexo': Select(attrs={'class':'form-control'}),
        }


class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control'}),
            'data_nasc': DateInput(attrs={'class':'form-control'}),
            'cpf': TextInput(attrs={'class':'form-control'}),
            'sexo': Select(attrs={'class':'form-control'}),
            'peso': NumberInput(attrs={'class':'form-control'}),
            'tamanho': NumberInput(attrs={'class':'form-control'}),
            'email': EmailInput(attrs={'class':'form-control'}),
            'telefone': TextInput(attrs={'class':'form-control'}),
            'grau_instrução': Select(attrs={'class':'form-control'}),
        }