from django.db import models

# Create your models here.
from django.db import models
from BackendPointage.accounts.models import User


class Horaire(models.Model):
    heureDebut = models.TimeField()
    heureFin = models.TimeField()
    joursTravail = models.JSONField()


"""class Pointage(models.Model):
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
#Model Pointage

import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

class QRCodeSession(models.Model):

    POINTAGE_TYPE = (
        ('ENTREE', 'Entrée'),
        ('SORTIE', 'Sortie'),
    )

    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    employey
     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type_pointage = models.CharField(max_length=10, choices=POINTAGE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=5)
        super().save(*args, **kwargs)


class Pointage(models.Model):

    employe = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    heure_entree = models.TimeField(null=True, blank=True)
    heure_sortie = models.TimeField(null=True, blank=True)

    est_retard = models.BooleanField(default=False)
    minutes_retard = models.IntegerField(default=0)
    heures_sup = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.employe.username} - {self.date}"


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
from django.db import models
from django.conf import settings

class Absence(models.Model):

    STATUT_CHOICES = (
        ('EN_ATTENTE', 'En attente'),
        ('VALIDE', 'Validée'),
        ('REJETE', 'Rejetée'),
    )

    TYPE_CHOICES = (
        ('CONGE_ANNUEL', 'Congé annuel'),
        ('MALADIE', 'Maladie'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dateDebut = models.DateField()
    dateFin = models.DateField()
    motif = models.TextField()
    typeAbsence = models.CharField(max_length=50, choices=TYPE_CHOICES)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='EN_ATTENTE')

    def __str__(self):
        return f"{self.user} - {self.statut}"