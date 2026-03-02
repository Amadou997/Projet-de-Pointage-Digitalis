from datetime import datetime, time
from django.utils import timezone
from pointage.models import Pointage, SemaineTravail
import calendar

DUREE_LEGALE = 40
PLAFOND_HEURES_SUP = 18


def calculer_heures(user, entree, sortie):

    duree = (sortie - entree).total_seconds() / 3600

    now = timezone.localtime()
    semaine = now.isocalendar()[1]
    annee = now.year

    semaine_obj, created = SemaineTravail.objects.get_or_create(
        user=user,
        semaine=semaine,
        annee=annee
    )

    semaine_obj.total_heures += duree

    if semaine_obj.total_heures <= DUREE_LEGALE:
        semaine_obj.heures_normales += duree
    else:
        heures_sup = semaine_obj.total_heures - DUREE_LEGALE

        if heures_sup <= 8:
            semaine_obj.heures_sup_15 += duree
        else:
            semaine_obj.heures_sup_40 += duree

    # Détection nuit
    if entree.time() >= time(21,0) or sortie.time() <= time(5,0):
        semaine_obj.heures_nuit += duree

    # Détection dimanche
    if now.weekday() == 6:
        semaine_obj.heures_dimanche += duree

    semaine_obj.save()

    return semaine_obj
def calculer_montant_heures_sup(user, semaine_obj):

    salaire_horaire = user.salaire_mensuel / 173.33

    montant = 0

    montant += semaine_obj.heures_sup_15 * salaire_horaire * 1.15
    montant += semaine_obj.heures_sup_40 * salaire_horaire * 1.40
    montant += semaine_obj.heures_nuit * salaire_horaire * 1.60
    montant += semaine_obj.heures_dimanche * salaire_horaire * 1.60

    return montant