import hmac
import hashlib
import time
import json
from django.conf import settings


def verify_qr(payload):
    secret = settings.SECRET_KEY.encode()

    signature = payload["signature"]
    message = f"{payload['employee_id']}{payload['timestamp']}".encode()

    expected_signature = hmac.new(secret, message, hashlib.sha256).hexdigest()

    return hmac.compare_digest(signature, expected_signature)