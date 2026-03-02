import hmac
import hashlib
import time
import json
from django.conf import settings


def verify_qr(payload):
/*
    """
    Verify the QR code signature to ensure it has not been tampered with.

    Parameters:
    payload (dict): A dictionary containing the QR code and its signature.

    Returns:
    bool: True if the signature is valid, False otherwise.


    secret = settings.SECRET_KEY.encode()

    signature = payload["signature"]
    message = f"{payload['employee_id']}{payload['timestamp']}".encode()

    expected_signature = hmac.new(secret, message, hashlib.sha256).hexdigest()

    return hmac.compare_digest(signature, expected_signature)