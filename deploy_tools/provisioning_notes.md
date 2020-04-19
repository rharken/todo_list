# Provisioning a new site
===

## Required packages:
* nginx
* Python 3.8
* virtualenv + pip * Git

eg, on Ubuntu:  
```bash
sudo apt update
sudo apt install nginx git python3.8 python3.8-venv
```

## Nginx Virtual Host config * see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com
* replace PATH with path of the source code

## Systemd service
* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com
* replace USER with username of the account
* replace PATH with path of the source code

## Folder structure:

Assume we have a user account at /home/username

/home/username  
└── sites  
    ├── DOMAIN1  
    │   ├── .env  
    │   ├── db.sqlite3  
    │   ├── manage.py etc  
    │   ├── static  
    │   └── virtualenv  
    └── DOMAIN2  
        ├── .env  
        ├── db.sqlite3  
        ├── etc  

