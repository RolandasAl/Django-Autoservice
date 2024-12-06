from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Automobilio_modelis, Automobilis, Paslauga,Uzsakymo_eilute,Uzsakymas,Busena
# Create your views here.

def index(request):
    num_paslauga = Paslauga.objects.all().count()
    num_automobiliai = Automobilis.objects.all().count()
    num_uzsakymu = Uzsakymas.objects.filter(status__pavadinimas='Įvykdytas').count()

    # perduodame informaciją į šabloną žodyno pavidale:
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'paslaugos': num_paslauga,
        'uzsakymai': num_uzsakymu,
        'automobiliai': num_automobiliai,
        'num_visits': num_visits,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)

def automobiliai(request):
    automobiliai_list = Automobilis.objects.all().order_by('id')
    paginator = Paginator(automobiliai_list, 2)
    page_number = request.GET.get('page')
    automobiliai = paginator.get_page(page_number)
    context = {
        'automobiliai':automobiliai
    }
    return render(request,'automobiliai.html',context=context)

def automobilis(request,masina_id):
    masina = get_object_or_404(Automobilis, pk=masina_id)
    return render(request,'automobilis.html',{'automobilis':masina})


class Uzsakymai(generic.ListView):
    model = Uzsakymas
    paginate_by = 2
    template_name = "uzsakymai.html"
    context_object_name = "uzsakymu_sarasas"
    ordering = ['id']

class Uzsakymo_info(generic.DetailView):
    model = Uzsakymas
    template_name = 'uzsakymas.html'


def search(request):
    query = request.GET.get('query')
    search_results = Automobilis.objects.filter(Q(klientas__icontains=query) | Q(valstybinis_nr__icontains=query) | Q(automobilio_modelis__modelis__icontains=query) | Q(vin_kodas__icontains=query) |Q(automobilio_modelis__marke__icontains=query))
    return render(request, 'search.html', {'automobiliai': search_results, 'query': query})

class User_uzsakymas(LoginRequiredMixin,generic.ListView):
    model = Uzsakymas
    template_name = 'user_uzsakymai.html'
    context_object_name = 'uzsakymu_sarasas'
    paginate_by = 5

    def get_queryset(self):
        return Uzsakymas.objects.filter(reader=self.request.user, status__pavadinimas='Įvykdytas').order_by('terminas')

