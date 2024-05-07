from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def index(request):
    return render(request, 'index.html')

def localizacao(request):
    return render(request, 'localizacao.html')


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})



def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'detalhes_produto.html', {'produto': produto})



def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'criar_produto.html', {'form': form})


from .forms import ProdutoForm


def atualizar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('detalhes_produto', produto_id=produto_id)
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'atualizar_produto.html', {'form': form})


def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'excluir_produto.html', {'produto': produto})

