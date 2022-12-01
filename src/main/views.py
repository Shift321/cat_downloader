from django.http import HttpResponse
from .tasks import *


def download(request):
    download_a_cat.delay()
    return HttpResponse('<h1>Загрузка кота!</h1>')
