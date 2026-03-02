import qrcode
import json
import hmac
import hashlib
from django.conf import settings
from django.core.files.base import ContentFile
from io import BytesIO


SECRET_KEY = settings.SECRET_KEY


def generate_qr_for_user(user):

    payload = {
        "user_id": user.id,
        "qr_uuid": str(user.qr_uuid),
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

    file_name = f"qr_user_{user.id}.png"

    user.qr_code_image.save(
        file_name,
        ContentFile(buffer.getvalue()),
        save=True
    )

    return user.qr_code_image.url