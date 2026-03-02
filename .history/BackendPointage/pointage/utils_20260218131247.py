import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

def generate_qr_image(token):

    qr = qrcode.make(token)

    buffer = BytesIO()
    qr.save(buffer, format='PNG')

    return ContentFile(buffer.getvalue(), name='qr.png')

