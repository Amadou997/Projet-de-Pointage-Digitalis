import qrcode
import json
import hmac
import hashlib
from io import BytesIO
from django.conf import settings
from django.core.files.base import ContentFile
from .models import QRDynamic

SECRET_KEY = settings.SECRET_KEY


def generate_dynamic_qr(user, type_pointage):

    # Création session QR en base
/*************  ✨ Windsurf Command ⭐  *************/
    """
    Génère un code QR dynamique associé à un employé et un type de pointage.

    Args:
        user (User): L'employé associé au code QR dynamique.
        type_pointage (str): Le type de pointage associé au code QR dynamique.

    Returns:
        dict: Un dictionnaire contenant l'image du code QR dynamique,
            le token associé au code QR dynamique, la date d'expiration
            du code QR dynamique et le nom du fichier de l'image.
    """
/*******  6c40f750-c7fc-4030-860e-303ed8ee734d  *******/
    qr_session = QRDynamic.objects.create(
        employe=user,
        type_pointage=type_pointage
    )

    payload = {
        "token": str(qr_session.token),
        "user_id": user.id,
        "nom": user.nom,
        "prenom": user.prenom,
        "type": type_pointage,
        "created_at": str(qr_session.created_at)
    }

    payload_json = json.dumps(payload)

    signature = hmac.new(
        SECRET_KEY.encode(),
        payload_json.encode(),
        hashlib.sha256
    ).hexdigest()

    final_payload = {
        "data": payload,
        "signature": signature
    }

    qr_data = json.dumps(final_payload)

    qr = qrcode.make(qr_data)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    file_name = f"dynamic_qr_{user.id}_{type_pointage}.png"

    return {
        "qr_image": buffer.getvalue(),
        "token": qr_session.token,
        "expires_at": qr_session.expires_at,
        "file_name": file_name
    }