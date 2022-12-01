from celery import shared_task
from django.conf import settings
import requests as r
import uuid

CAT_URL = "https://cataas.com/cat"


@shared_task
def download_a_cat():
    """
    Celery task
    """
    resp = r.get(CAT_URL)
    file_ext = resp.headers.get('Content-type').split('/')[1]
    file_name = settings.BASE_DIR / 'cats' / (str(uuid.uuid4()) + "." + file_ext)
    with open(file_name, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=128):
            f.write(chunk)
