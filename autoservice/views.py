from django.shortcuts import render

from .models import Automobilio_modelis, Automobilis, Paslauga,Uzsakymo_eilute,Uzsakymas,Busena
# Create your views here.

def index(request):
    num_paslauga = Paslauga.objects.all().count()
    num_automobiliai = Automobilis.objects.all().count()
    num_uzsakymu = Uzsakymas.objects.filter(status__pavadinimas='Įvykdytas').count()

    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'paslaugos': num_paslauga,
        'uzsakymai': num_uzsakymu,
        'automobiliai': num_automobiliai
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)