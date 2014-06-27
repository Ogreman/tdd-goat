Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenvwrapper

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenvwrapper
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.4
    source /usr/local/bin/virtualenvwrapper.sh 
    mkvirtualenv SITENAME --python=/usr/bin/python3.4
    pip install -r requirements.txt    

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com
* replace USER with username

## Folder structure:
Assume we have a user account at /home/USER

/home/USER
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv
