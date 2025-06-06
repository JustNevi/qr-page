FROM python:3.12-slim

WORKDIR /opt/qr-page/

COPY requirements.dev.txt .
RUN python3 pip install -r requirements.dev.txt

COPY qr_page .
RUN cd qr_page \
	&& python3 ./qr_page/manage.py makemigration \
	&& python3 ./qr_page/manage.py migrate 

