.PHONY: hello runserver migrate makemigrations

manage := ./qr_page/manage.py

hello:
	echo "Hello. Manage file in ${manage}"

migrate:
	python ${manage} migrate

makemigrations:
	python ${manage} makemigrations 

runserver:
	python ${manage} runserver