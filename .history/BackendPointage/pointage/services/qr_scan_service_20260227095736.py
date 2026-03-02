from pointage.models import Pointage
from datetime import datetime, time
from django.utils import timezone
from django.db.models import Sum
from .services.calcul_service import calculer_pointage

if data["type"] == "SORTIE":

    entree_du_jour = Pointage.objects.filter(
        user=qr_instance.employe,
        date=timezone.now().date(),
        type_pointage="ENTREE"
    ).last()

    if not entree_du_jour:
        return {"error": "Aucune entrée trouvée"}

    calcul = calculer_pointage(
        qr_instance.employe,
        entree_du_jour.heure,
        heure_actuelle
    )

    pointage.heures_travaillees = calcul["heures_travaillees"]
    pointage.heures_supplementaires = calcul["heures_supplementaires"]
    pointage.montant_heures_sup = calcul["montant_heures_sup"]
    pointage.retard = calcul["retard"]
    pointage.save()