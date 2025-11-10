# Deploy

## Development

### Minikube

#### Create namespace

`kubectl create namespace development`

#### Clone project

```
git clone -b main https://github.com/JustNevi/qr-page.git back
git clone -b front https://github.com/JustNevi/qr-page.git front
git clone -b k8s https://github.com/JustNevi/qr-page.git k8s
```

#### Build docker images

Backend Django:

```
cd back
docker build -t qr-django .
minikube image load qr-django
cd ..
```

Frontend React:

```
cd front
docker build -t qr-react .
minikube image load qr-react
cd ..
```

#### Configure your sercrets

Create \*-secrets

```
cd k8s
touch mysql-secret.yaml
touch minio-secret.yaml
touch qr-django-secret.yaml
touch qr-react-secret.yaml
```

and configre them.

#### Configure Caddy Ingress Controller

1. Enable Minikube Ingress Addon

```bash
minikube addons enable ingress
```

2. Install Helm

   To install Caddy you need [Helm](https://helm.sh/). Installation guide for Helm [here](https://helm.sh/docs/intro/install/).

3. Install Caddy

   Than you need install [Caddy](https://github.com/caddyserver/ingress).

#### Apply all components

In k8s directory run:

```
# Mysql
kubectl apply -f mysql-config.yaml
kubectl apply -f mysql-secret.yaml
kubectl apply -f mysql.yaml
```

```
# MinIO
kubectl apply -f minio-secret.yaml
kubectl apply -f minio-dev.yaml
```

```
# Django
kubectl apply -f qr-django-config.yaml
kubectl apply -f qr-django-secret.yaml
kubectl apply -f qr-django.yaml
```

```
# React
kubectl apply -f qr-react-secret.yaml
kubectl apply -f qr-react.yaml
```

```
# Ingress
kubectl apply -f ingress.yaml
```

or

```
make apply_all
```

#### Connect

You'll need to configure your `/etc/hosts` file to resolve the application hostnames.

Get minikube ip:

```bash
minikube ip
#192.168.49.2
```

```bash
sudo vim /etc/hosts # or your preferred editor
```

Add the following line (replace the IP with your Minikube IP):

```
192.168.49.2  django.qr-page.local
192.168.49.2  react.qr-page.local
```
