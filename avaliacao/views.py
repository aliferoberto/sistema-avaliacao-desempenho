from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Avaliacao, Colaborador, Nota
from .forms import AvaliacaoForm, NotaForm

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def lista_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})

@login_required
def detalhe_avaliacao(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id)
    notas = Nota.objects.filter(avaliacao=avaliacao)

    return render(request, 'detalhe_avaliacao.html', {
        'avaliacao': avaliacao,
        'notas': notas
    })

@login_required
def criar_avaliacao(request):
    try:
        colaborador = Colaborador.objects.get(user=request.user)
    except Colaborador.DoesNotExist:
        messages.error(request, 'Seu usuário não está vinculado a um colaborador.')
        return redirect('home')

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.avaliador = colaborador
            avaliacao.save()
            return redirect('lista_avaliacoes')
    else:
        form = AvaliacaoForm()

    return render(request, 'criar_avaliacao.html', {'form': form})

@login_required
def adicionar_nota(request, avaliacao_id):
    avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id)

    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.avaliacao = avaliacao
            nota.save()
            return redirect('detalhe_avaliacao', id=avaliacao.id)
    else:
        form = NotaForm()

    return render(request, 'adicionar_nota.html', {
        'form': form,
        'avaliacao': avaliacao
    })

@login_required
def excluir_avaliacao(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id)
    avaliacao.delete()
    return redirect('lista_avaliacoes')