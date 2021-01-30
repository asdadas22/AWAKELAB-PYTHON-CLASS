from django.shortcuts import render

# Create your views here.

def primeraPagina(request):
    return render(request, 'app_ex_html/home.html')
