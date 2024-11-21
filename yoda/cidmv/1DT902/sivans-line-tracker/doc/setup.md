# Setting up Nginx, SQLite, Flask and deploying Linux server
## Prerequisites
- A Linux server running on Ubuntu distro and with SSH access

## Step 1: Install required software
### Nginx
```bash
sudo apt update
sudo apt install nginx
```

### SQLite
SQLite is a serverless database engine which you will no need to install


### Flask (Assuming Python is installed)
```bash
pip install Flask
```

## Step 2: Configure Nginx
Change "your_domain_or_ip" to the Linux servers ip or if you have the a domain name

```bash
sudo nano /etc/nginx/sites-available/your_flask_app.conf
```

```bash
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:your_flask_app_port;
        include /etc/nginx/proxy_params;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
```

```bash
sudo ln -s /etc/nginx/sites-available/your_flask_app.conf /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart your_flask_app
```

## Step 3: Configure Flask for Nginx
For this gunicorn is needed to be installed and configured
```bash
sudo mkdir sivans

cd sivans

python -m venv venv

source venv/bin/activate

pip install gunicorn

deactivate

sudo nano /etc/systemd/system/your_flask_app.service
```

```bash
[Unit]
Description=Gunicorn instance to serve Flask app
After=network.target

[Service]
User=host
Group=www-data
WorkingDirectory=/home/host/sivans
ExecStart=/home/host/venv/bin/gunicorn -c /home/host/gunicorn.conf.py wsgi:app

[Install]
WantedBy=multi-user.target
```

```bash
sudo nano gunicorn.conf.py
```

```bash
bind = "0.0.0.0:5000"
workers = 3
wsgi_app = "wsgi:app"
```

## Step 4: Create Flask app
```bash
mkdir app
cd app
```

In this folder add the following files from gitlab repository:
- app.py
- wsgi.py
- configs.py
- db_manger.py

Add the following folders from the gitlab repository in the app folder:
- templates
- static

## Step 5: Start the app
```bash
sudo systemctl reload-daemon
sudo systemctl start your_flask_app
```