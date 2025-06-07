FROM python:3.12-slim

WORKDIR /opt/qr_page/

# Install dependency
RUN apt-get update \  
	&& apt-get install -y pkg-config python3-dev default-libmysqlclient-dev build-essential

# Install requirements
COPY requirements.prod.txt .
RUN python3 -m pip install -r requirements.prod.txt

# Copy project 
COPY qr_page qr_page
COPY local/settings.prod.py local/settings.prod.py

EXPOSE 8000

CMD ["python3", "./qr_page/manage.py", "runserver", "0.0.0.0:8000"]
