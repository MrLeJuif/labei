from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('follow_up:accueil'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed !")
            print(f"Username : {username} and password {password}")
            return HttpResponse("Vos identifiants sont incorrects")
    else:
        return render(request, 'follow_up/index.html', {})


class IndexView(TemplateView):
    template_name = 'follow_up/accueil.html'
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJTECTION'
        return context
    '''


class MemberListView(ListView):
    context_object_name = 'membres'
    model = models.Membre
    template_name = 'follow_up/membre_liste.html'


class MemberDetailView(DetailView):
    context_object_name = 'membre_details'
    model = models.Membre
    template_name = 'follow_up/membre_details.html'


class MembreCreateView(CreateView):
    fields = ('nom_membre', 'prenom_membre', 'numero_membre',
              'adresse_membre', 'role_membre', 'basonta_membre',
              'bacenta_membre', 'branche_membre', 'bapteme_esprit', 'bapteme_eau')
    model = models.Membre
    template_name = 'follow_up/membre_form.html'


class MembreUpdateView(UpdateView):
    fields = ('nom_membre', 'prenom_membre', 'numero_membre',
              'adresse_membre', 'role_membre', 'basonta_membre',
              'bacenta_membre', 'branche_membre', 'bapteme_esprit', 'bapteme_eau')
    model = models.Membre


class MembreDeleteView(DeleteView):
    model = models.Membre
    success_url = reverse_lazy("follow_up:list")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('follow_up:index'))


# Bergers
class BergerListView(ListView):
    context_object_name = 'membres'
    model = models.Membre
    template_name = 'bergers/berger_liste.html'


# Pasteur
class PasteurListView(ListView):
    context_object_name = 'membres'
    model = models.Membre
    template_name = 'pasteurs/pasteur_liste.html'


# Basonta
class BasontaListView(ListView):
    context_object_name = 'basontas'
    model = models.Basonta
    template_name = 'basontas/basonta_liste.html'


class BasontaDetailView(DetailView):
    context_object_name = 'basonta_details'
    model = models.Basonta
    template_name = 'basontas/basonta_details.html'


# Bacenta
class BacentaListView(ListView):
    context_object_name = 'bacentas'
    model = models.Bacenta
    template_name = 'bacentas/bacenta_liste.html'


class BacentaDetailView(DetailView):
    context_object_name = 'bacenta_details'
    model = models.Bacenta
    template_name = 'bacentas/bacenta_details.html'


# Branche
class BrancheListView(ListView):
    context_object_name = 'branches'
    model = models.Branche
    template_name = 'branches/branche_liste.html'


class BrancheDetailView(DetailView):
    context_object_name = 'branche_details'
    model = models.Branche
    template_name = 'branches/branche_details.html'


# Rapports
# Listes
class BasontaRapportListView(ListView):
    context_object_name = 'basonta_rapports'
    model = models.Basonta_rapport
    template_name = 'follow_up/membre_liste.html'


class BacentaRapportListView(ListView):
    context_object_name = 'bacenta_rapports'
    model = models.Bacenta_week
    template_name = 'follow_up/membre_liste.html'


class SundayListView(ListView):
    context_object_name = 'sunday_rapports'
    model = models.Bacenta_sunday
    template_name = 'follow_up/membre_liste.html'


# Creation
class BasontaRapportCreateView(CreateView):
    fields = ('date', 'basonta', 'theme', 'enfant', 'adulte', 'nouveau', 'offrande')
    model = models.Basonta_rapport
    template_name = 'rapports/basonta_rapport_form.html'


class BacentaRapportCreateView(CreateView):
    fields = ('date', 'bacenta', 'theme', 'enfant', 'adulte', 'nouveau', 'nee_de_nouveau', 'offrande')
    model = models.Bacenta_week
    template_name = 'rapports/bacenta_rapport_form.html'


class SundayRapportCreateView(CreateView):
    fields = ('date', 'bacenta', 'enfant', 'adulte', 'nouveau', 'offrande', 'transport')
    model = models.Bacenta_sunday
    template_name = 'rapports/sunday_rapport_form.html'


# Update
class BasontaRapportUpdateView(UpdateView):
    fields = ('date', 'basonta', 'theme', 'enfant', 'adulte', 'nouveau', 'offrande')
    model = models.Basonta_rapport


class BacentaRapportUpdateView(UpdateView):
    fields = ('date', 'basonta', 'theme', 'enfant', 'adulte', 'nouveau', 'offrande')
    model = models.Bacenta_week


class SundayRapportUpdateView(UpdateView):
    fields = ('date', 'basonta', 'theme', 'enfant', 'adulte', 'nouveau', 'offrande')
    model = models.Bacenta_sunday