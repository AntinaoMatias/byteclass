from django.shortcuts import render

# Create your views here.

def bienvenida(request):
    return render(request, 'byteclass/index.html')

def error_404(request, exception):
    return render(request, 'byteclass/404.html', status=404)