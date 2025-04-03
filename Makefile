.PHONY: hello runserver migrate makemigrations

manage := ./qr_page/manage.py

hello:
	echo "Hello. Manage file in ${manage}"

temp_to_local_dev_settings:
	mkdir -p local
	cp qr_page/qr_page/settings/templates/settings.dev.py local/settings.dev.py

migrate:
	python ${manage} migrate

makemigrations:
	python ${manage} makemigrations 

runserver:
	python ${manage} runserver