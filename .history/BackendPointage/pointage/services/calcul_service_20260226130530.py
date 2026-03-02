from datetime import datetime, time
from django.utils import timezone
from django.db.models import Sum
from pointage.models import Pointage


HEURE_ENTREE_LEGALE = time(9, 0)
HEURE_SORTIE_LEGALE = time(17, 0)


def calculer_pointage(user, heure_entree, heure_sortie):

    retard = heure_entree > HEURE_ENTREE_LEGALE

    # Calcul heures normales
    delta = datetime.combine(timezone.now().date(), heure_sortie) - \
            datetime.combine(timezone.now().date(), heure_entree)

    heures_travaillees = delta.total_seconds() / 3600

    heures_sup_jour = 0

    if heure_sortie > HEURE_SORTIE_LEGALE:
        delta_sup = datetime.combine(timezone.now().date(), heure_sortie) - \
                    datetime.combine(timezone.now().date(), HEURE_SORTIE_LEGALE)
        heures_sup_jour = delta_sup.total_seconds() / 3600

    # Total semaine
    semaine_total = Pointage.objects.filter(
        user=user,
        date__week=timezone.now().date().isocalendar()[1]
    ).aggregate(total=Sum("heures_travaillees"))["total"] or 0

    semaine_total += heures_travaillees

    heures_sup_semaine = 0

    if semaine_total > 40:
        heures_sup_semaine = semaine_total - 40

    # Calcul salaire horaire
    salaire_horaire = user.salaire_mensuel / 173.33

    montant_sup = 0

    if 40 < semaine_total <= 48:
        montant_sup = heures_sup_semaine * salaire_horaire * 1.15
    elif semaine_total > 48:
        montant_sup = heures_sup_semaine * salaire_horaire * 1.40

    return {
        "retard": retard,
        "heures_travaillees": heures_travaillees,
        "heures_supplementaires": heures_sup_semaine,
        "montant_heures_sup": montant_sup
    }