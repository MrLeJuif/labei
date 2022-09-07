from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    nom_role = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.nom_role


class Basonta(models.Model):
    nom_basonta = models.CharField(max_length=256, unique=True)
    leader_basonta = models.CharField(max_length=256, default='Aucun')

    def __str__(self):
        return self.nom_basonta


class Bacenta(models.Model):
    nom_bacenta = models.CharField(max_length=256, unique=True)
    leader_bacenta = models.CharField(max_length=256, default='Aucun')

    def __str__(self):
        return self.nom_bacenta


class Branche(models.Model):
    nom_branche = models.CharField(max_length=256, unique=True)
    leader_branche = models.CharField(max_length=256, default='Aucun')

    def __str__(self):
        return self.nom_branche


class Membre(models.Model):
    nom_membre = models.CharField(max_length=256)
    prenom_membre = models.CharField(max_length=256)
    numero_membre = models.PositiveIntegerField()
    adresse_membre = models.CharField(max_length=256)
    role_membre = models.ForeignKey(Role, on_delete=models.DO_NOTHING, )
    basonta_membre = models.ForeignKey(Basonta, related_name='basontas', on_delete=models.DO_NOTHING,)
    bacenta_membre = models.ForeignKey(Bacenta, related_name='bacentas', on_delete=models.DO_NOTHING,)
    branche_membre = models.ForeignKey(Branche, related_name='branches', on_delete=models.DO_NOTHING,)
    bapteme_esprit = models.BooleanField()
    bapteme_eau = models.BooleanField()
    date_ajout_membre = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.nom_membre

    def get_absolute_url(self):
        return reverse('follow_up:details', kwargs={'pk':self.pk})


class Basonta_rapport(models.Model):
    date = models.DateField(default=datetime.date.today)
    basonta = models.ForeignKey(Basonta, related_name='basontas_rapport', on_delete=models.DO_NOTHING,)
    theme = models.CharField(max_length=256)
    enfant = models.PositiveSmallIntegerField(default=0)
    adulte = models.PositiveSmallIntegerField(default=0)
    nouveau = models.PositiveSmallIntegerField(default=0)
    offrande = models.PositiveIntegerField(default=0)
    date_ajout_rapport = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.date


class Bacenta_week(models.Model):
    date = models.DateField(default=datetime.date.today)
    bacenta = models.ForeignKey(Bacenta, related_name='bacentas_rapport_week', on_delete=models.DO_NOTHING, )
    theme = models.CharField(max_length=256)
    enfant = models.PositiveSmallIntegerField(default=0)
    adulte = models.PositiveSmallIntegerField(default=0)
    nouveau = models.PositiveSmallIntegerField(default=0)
    nee_de_nouveau = models.PositiveSmallIntegerField(default=0)
    offrande = models.PositiveIntegerField(default=0)
    date_ajout_rapport = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.date


class Bacenta_sunday(models.Model):
    date = models.DateField(default=datetime.date.today)
    bacenta = models.ForeignKey(Basonta, related_name='basontas_rapport_sunday', on_delete=models.DO_NOTHING, )
    enfant = models.PositiveSmallIntegerField(default=0)
    adulte = models.PositiveSmallIntegerField(default=0)
    nouveau = models.PositiveSmallIntegerField(default=0)
    offrande = models.PositiveIntegerField(default=0)
    transport = models.PositiveIntegerField(default=0)
    date_ajout_rapport = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.date