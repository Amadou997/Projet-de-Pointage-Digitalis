from django.db import models

# Create your models here.
from django.db import models
from BackendPointage.accounts.models import User


class Horaire(models.Model):
    heureDebut = models.TimeField()
    heureFin = models.TimeField()
    joursTravail = models.JSONField()


class Pointage(models.Model):
    TYPE_CHOICES = [
        ("ENTREE", "Entrée"),
        ("SORTIE", "Sortie"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    heure = models.TimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    localisation = models.CharField(max_length=255)

"""
class Absence(models.Model):
    STATUT_CHOICES = [
        ("EN_ATTENTE", "En attente"),
        ("VALIDE", "Validé"),
        ("REJETE", "Rejeté"),
    ]

    TYPE_CHOICES = [
        ("CONGE_ANNUEL", "Congé annuel"),
        ("MALADIE", "Maladie"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateDebut = models.DateField()
    dateFin = models.DateField()
    motif = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="EN_ATTENTE")
    typeAbsence = models.CharField(max_length=30, choices=TYPE_CHOICES)

    """
