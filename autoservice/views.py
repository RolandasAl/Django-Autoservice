from django.shortcuts import render,get_object_or_404
from django.views import generic
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

def automobiliai(request):
    automobiliai = Automobilis.objects.all()
    context = {
        'automobiliai':automobiliai
    }
    print(automobiliai)
    return render(request,'automobiliai.html',context=context)

def automobilis(request,masina_id):
    masina = get_object_or_404(Automobilis, pk=masina_id)
    return render(request,'automobilis.html',{'automobilis':masina})


class Uzsakymai(generic.ListView):
    model = Uzsakymas
    template_name = "uzsakymai.html"
    context_object_name = "uzsakymu_sarasas"

class Uzsakymo_info(generic.DetailView):
    model = Uzsakymas
    template_name = 'uzsakymas.html'