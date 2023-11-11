from django.shortcuts import render
from passagens.forms import PassagensForm

# Create your views here.
def index(request):
    form = PassagensForm
    context = {'form':form}
    return render(request,'index.html',context)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagensForm(request.POST)
        if form.is_valid():
            context = {'form':form} 
            return render(request,'minha_consulta.html',context)
        else:
            print("Informações invalidas")
            context = {'form':form} 
            return render(request,'index.html',context)

    
def confirmar_viagem(request):
    return render(request,'confirmar.html')

