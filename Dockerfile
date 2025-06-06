FROM python:3.12-slim

WORKDIR /opt/qr_page/

# Install dependency
RUN apt-get update \  
	&& apt-get install -y pkg-config python3-dev default-libmysqlclient-dev build-essential

# Install requirements
COPY requirements.dev.txt .
RUN python3 -m pip install -r requirements.prod.txt

# Copy project 
COPY qr_page qr_page
COPY local/settings.prod.py local/settings.prod.py

# Prepare project for run
RUN cd ./qr_page \
	&& python3 manage.py makemigrations \
	&& python3 manage.py migrate 

EXPOSE 8000

CMD python3 manage.py runserver
