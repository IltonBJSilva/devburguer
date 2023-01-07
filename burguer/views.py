from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'burguer/home.html')

def detalhe_produto(request):
	return render(request, 'burguer/produto.html')