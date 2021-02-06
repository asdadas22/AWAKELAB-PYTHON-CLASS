from django.shortcuts import render

# Create your views here.

def home_page(request):
    context = {"one": "uno", 
    "two": "dos", 
    "three": "tres", 
    "four": "cuatro",
    "five":" cinco"}
    return render(request, 'miapp/home.html', context)

def extra_page(request):
    return render(request, 'miapp/extra.html')