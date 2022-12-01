# Cats Downloader
Простое приложение для скачивания фотографий котов с использованием Celery и Django

## Установка и запуск приложения

Скачать репозиторий, перейти в директорию src
```bash
python manage.py makemigrations
python manage.py migrate
docker-compose up
```
## Функционал
Коты скачиваются в директорию cats, чтобы начать скачивание 
после запуска приложения нужно перейти по url 128.0.0.1:8000/download
после чего можно обновить страницу огромное количество раз и все скачивания встанут в очередь в celery и будут постепенно скачиваться

## View

Основная view , которая отдает задачу в селери.
```python
def download(request):
    download_a_cat.delay()
    return HttpResponse('<h1>Загрузка кота!</h1>')
```
## Celery settings
Файл с настрйоками celery.py
```python
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

app = Celery('src')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
```

## Tasks
Задача , которая скачивает кота
```python
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
```


## Стак технологий

<a href="">
    <img src="https://img.shields.io/badge/django-4.1.3-yellowgreen" alt="Django Badge"/>
    <img src="https://img.shields.io/badge/%D0%A1elery-5.2.7-blue" alt="Celery Badge"/>
</a>

## Ресурсы 

```
https://cataas.com/cat
```