FROM python:3.10.8
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src ./src

CMD [ "python3","./project/manage.py", "runserver", "0.0.0.0:8000"]