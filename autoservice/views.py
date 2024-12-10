from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render,get_object_or_404,reverse
from django.views import generic
from django.views.generic.edit import FormMixin
from .forms import UzsakymasReviewForm
from .models import Automobilio_modelis, Automobilis, Paslauga,Uzsakymo_eilute,Uzsakymas,Busena
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .forms import UzsakymasReviewForm, UserUpdateForm, ProfilisUpdateForm
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

class Uzsakymo_info(FormMixin,generic.DetailView):
    model = Uzsakymas
    template_name = 'uzsakymas.html'
    form_class = UzsakymasReviewForm

    # nurodome, kur atsidursime komentaro sėkmės atveju.
    def get_success_url(self):
        return reverse('uzsakymo_info', kwargs={'pk': self.object.id})

    # standartinis post metodo perrašymas, naudojant FormMixin, galite kopijuoti tiesiai į savo projektą.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # štai čia nurodome, kad knyga bus būtent ta, po kuria komentuojame, o vartotojas bus tas, kuris yra prisijungęs.
    def form_valid(self, form):
        form.instance.uzsakymas = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(Uzsakymo_info, self).form_valid(form)


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

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')

@login_required
def profilis(request):
    return render(request, 'profilis.html')



@login_required
def profilis(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilisUpdateForm(request.POST, request.FILES, instance=request.user.profilis)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('profilis')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilisUpdateForm(instance=request.user.profilis)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profilis.html', context)