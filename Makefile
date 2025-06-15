.PHONY: apply_mysql apply_minio apply_django apply_react apply_ingress apply_all
	
apply_mysql:
	echo "Applying config, secret, deployment for mysql"
	kubectl apply -f mysql-config.yaml
	sleep 3
	kubectl apply -f mysql-secret.yaml
	sleep 3
	kubectl apply -f mysql.yaml

apply_minio:
	echo "Applying secret, deployment for minio"
	kubectl apply -f minio-secret.yaml
	sleep 3
	kubectl apply -f minio-dev.yaml

apply_django:
	echo "Applying config, secret, deployment for django"
	kubectl apply -f qr-django-config.yaml
	sleep 3
	kubectl apply -f qr-django-secret.yaml
	sleep 3
	kubectl apply -f qr-django.yaml

apply_react:
	echo "Applying secret, deployment for react"
	kubectl apply -f qr-react-secret.yaml
	sleep 3
	kubectl apply -f qr-react.yaml

apply_ingress:
	echo "Applying ingress"
	kubectl apply -f ingress.yaml

apply_all:
	$(MAKE) apply_mysql
	sleep 5 # Wait for 5 seconds after MySQL
	$(MAKE) apply_minio
	sleep 5 # Wait for 5 seconds after MinIO 
	$(MAKE) apply_django
	sleep 10 # Wait for 10 seconds after Django
	$(MAKE) apply_react
	sleep 5 # Wait for 5 seconds after React
	$(MAKE) apply_ingress


.PHONY: delete_mysql delete_minio delete_django delete_react delete_ingress delete_all

delete_mysql:
	echo "Deleting config, secret, deployment for mysql"
	kubectl delete -f mysql.yaml
	kubectl delete -f mysql-secret.yaml
	kubectl delete -f mysql-config.yaml

delete_minio:
	echo "Deleting secret, deployment for minio"
	kubectl apply -f minio-dev.yaml
	kubectl apply -f minio-secret.yaml
	
delete_django:
	echo "Deleting config, secret, deployment for django"
	kubectl delete -f qr-django.yaml
	kubectl delete -f qr-django-secret.yaml
	kubectl delete -f qr-django-config.yaml

delete_react:
	echo "Deleting secret, deployment for react"
	kubectl delete -f qr-react.yaml
	kubectl delete -f qr-react-secret.yaml

delete_ingress:
	echo "Deleting ingress"
	kubectl delete -f ingress.yaml

delete_all:
	$(MAKE) delete_mysql
	sleep 1 # Wait for 1 seconds after MySQL
	$(MAKE) delete_minio
	sleep 1 # Wait for 1 seconds after MinIO 
	$(MAKE) delete_django
	sleep 1 # Wait for 1 seconds after Django
	$(MAKE) delete_react
	sleep 1 # Wait for 1 seconds after React
	$(MAKE) delete_ingress
