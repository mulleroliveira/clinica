from django.shortcuts import render, redirect
from . models import Cliente
from . models import Medico
from . forms import ClienteForm, MedicoForm

def home(request):
    return render(request, 'home.html', {})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request,'cliente/list.html', {'clientes':clientes})

def cliente_show(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    return render(request, 'cliente/show.html', {'cliente':cliente})

def cliente_form(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/atendimento/cliente/')
        else:
            return render(request, 'cliente/form.html', {'form':form})
    else:
        form = ClienteForm()
        return render(request, 'cliente/form.html', {'form':form})

def cliente_edit(request, cliente_id):
    if request.method == 'POST':
        cliente = Cliente.objects.get(pk=cliente_id)
        form = ClienteForm(request.POST, instance=cliente)
        if (form.is_valid()):
            form.save()
            return redirect('/atendimento/cliente/')
        else:
            return render(request, 'cliente/edit.html', {'form':form, 'cliente_id':cliente_id})
    else:
        cliente = Cliente.objects.get(pk=cliente_id)
        form = ClienteForm(instance=cliente)
        return render(request, 'cliente/edit.html', {'form':form, 'cliente_id':cliente_id})

def medico_list(request):
    medicos = Medico.objects.all()
    return render(request,'medico/list.html', {'medicos':medicos})

def medico_show(request, medico_id):
    medico = Medico.objects.get(pk=medico_id)
    return render(request, 'medico/show.html', {'medico':medico})

def medico_form(request):
    if request.method == "POST":
        form = MedicoForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/atendimento/medico')
        else:
            return render(request, 'medico/form.html', {'form':form})
    else:
        form = MedicoForm()
        return render(request, 'medico/form.html', {'form':form})

def medico_edit(request, medico_id):
    if request.method == 'POST':
        medico = Medico.objects.get(pk=medico_id)
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('/atendimento/medico/')
        else:
            return render(request, 'medico/edit.html', {'form':form, 'medico_id':medico_id})
    else:
        medico = Medico.objects.get(pk=medico_id)
        form = MedicoForm(instance=medico)
        return render(request, 'medico/edit.html', {'form':form, 'medico_id':medico_id})