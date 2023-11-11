from django import forms
from datetime import datetime
from passagens.classes_viagens import tipos_de_classes
from passagens.validation import *

class PassagensForm(forms.Form):
    origem = forms.CharField(max_length=100,label='Origem',widget=forms.TextInput(attrs={'style': 'text-transform: capitalize;'}))
    destino = forms.CharField(max_length=100,label='Destino',widget=forms.TextInput(attrs={'style': 'text-transform: capitalize;'}))
    ida = forms.DateField(widget=forms.SelectDateWidget(),label='Ida',initial=datetime.today)
    data_hoje = forms.DateField(label='Dia atual',disabled=True,initial=datetime.today)
    volta = forms.DateField(widget=forms.SelectDateWidget(),label='Volta',initial=datetime.today)
    classe = forms.ChoiceField(label='Classe do voo',choices=tipos_de_classes)


    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        ida = self.cleaned_data.get('ida')
        volta = self.cleaned_data.get('volta')
        data_hoje = self.cleaned_data.get('volta')
        lista_de_erro = {}

        campo_tem_numero(origem,'origem',lista_de_erro)
        campo_tem_numero(destino,'destino',lista_de_erro)
        origem_destino_iguais(origem,destino,lista_de_erro)
        data_ida_maior_data_volta(ida,volta,lista_de_erro)
        data_ida_menor_data_hoje(ida,data_hoje,lista_de_erro)

        if lista_de_erro is not None:
            for erro in lista_de_erro:
                mensagem_erro = lista_de_erro[erro]
                self.add_error(erro,mensagem_erro)
        return self.cleaned_data


 
