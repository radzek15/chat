FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN mkdir /CV_site

WORKDIR /CV_site

COPY . /CV_site

RUN pip install -r requirements.txt

RUN python manage.py makemigrations chat && python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]