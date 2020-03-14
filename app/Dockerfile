FROM python:3.7

COPY . /app/

RUN pip install -r app/requirements.txt

RUN mv app/wsgi.py wsgi.py

CMD python wsgi.py