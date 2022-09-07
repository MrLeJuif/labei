from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


app_name = 'follow_up'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', login_required(views.IndexView.as_view()), name='accueil'),
    path('logout/', login_required(views.user_logout), name='user_logout'),
    path('follow_up/', login_required(views.MemberListView.as_view()), name='list'),
    # path('follow_up/', views.MemberListView.as_view(), name='list'),
    path('follow_up/<int:pk>/', login_required(views.MemberDetailView.as_view()), name='details'),
    path('follow_up/ajout_membre/', login_required(views.MembreCreateView.as_view()), name='create'),
    path('follow_up/modifier_membre/<int:pk>/', login_required(views.MembreUpdateView.as_view()), name='update'),
    path('follow_up/supprimer_membre/<int:pk>/', login_required(views.MembreDeleteView.as_view()), name='delete'),
    # Bergers
    path('bergers/', login_required(views.BergerListView.as_view()), name='berger_list'),
    path('bergers/<int:pk>/', login_required(views.MemberDetailView.as_view()), name='berger_details'),
    # Pasteurs
    path('pasteurs/', login_required(views.PasteurListView.as_view()), name='pasteur_list'),
    path('pasteurs/<int:pk>/', login_required(views.MemberDetailView.as_view()), name='pasteur_details'),
    # Basontas
    path('basontas/', login_required(views.BasontaListView.as_view()), name='basonta_list'),
    path('basontas/<int:pk>/', login_required(views.BasontaDetailView.as_view()), name='basonta_details'),
    # Bacentas
    path('bacentas/', login_required(views.BacentaListView.as_view()), name='bacenta_list'),
    path('bacentas/<int:pk>/', login_required(views.BacentaDetailView.as_view()), name='bacenta_details'),
    # Branches
    path('branches/', login_required(views.BrancheListView.as_view()), name='branche_list'),
    path('branches/<int:pk>/', login_required(views.BrancheDetailView.as_view()), name='branche_details'),
    #Rapprots
    path('follow_up/ajout_rapport1/', login_required(views.BasontaRapportCreateView.as_view()), name='create_basonta_rapport'),
    path('follow_up/ajout_rapport2/', login_required(views.BacentaRapportCreateView.as_view()), name='create_bacenta_rapport'),
    path('follow_up/ajout_rapport3/', login_required(views.SundayRapportCreateView.as_view()), name='create_sunday_rapport'),
]