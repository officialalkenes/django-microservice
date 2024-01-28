FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.in /app/requirements.in

RUN pip install --upgrade pip && pip install -r requirements.in
COPY . /app

CMD [ "python manage.py runserver 0.0.0.0:8000" ]
