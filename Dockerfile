FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN pip install -U 'pip > 9'

RUN mkdir /app
RUN mkdir -p /tmp/wheel

ADD . /app

WORKDIR /app

RUN pip install --find-links=wheel/ --no-cache-dir -r requirements.txt
RUN pip install .

# CMD python manage.py runserver 0.0.0.0:8000
CMD gunicorn arnica.wsgi:application --log-file - -b 0.0.0.0:8000

EXPOSE 8000
