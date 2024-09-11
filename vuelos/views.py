from django.shortcuts import render, redirect
from .forms import VueloForm
from .models import Vuelo
from django.db.models import Avg

def index(request):
    return render(request, 'vuelos/index.html')

def registrar_vuelo(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vuelos')
    else:
        form = VueloForm()

    return render(request, 'vuelos/registrar_vuelo.html', {'form': form})

def listar_vuelos(request):
    vuelos = Vuelo.objects.all().order_by('precio')
    return render(request, 'vuelos/listar_vuelos.html', {'vuelos': vuelos})

def estadisticas_vuelos(request):
    vuelos_nacionales = Vuelo.objects.filter(tipo='Nacional').count()
    vuelos_internacionales = Vuelo.objects.filter(tipo='Internacional').count()
    precio_promedio_nacionales = Vuelo.objects.filter(tipo='Nacional').aggregate(Avg('precio'))['precio__avg']

    return render(request, 'vuelos/estadisticas_vuelos.html', {
        'vuelos_nacionales': vuelos_nacionales,
        'vuelos_internacionales': vuelos_internacionales,
        'precio_promedio_nacionales': precio_promedio_nacionales,
    })


