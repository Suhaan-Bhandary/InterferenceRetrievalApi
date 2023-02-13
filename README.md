# Inference based retrieval in own using NLP

## Project Setup

Prerequisites

1. python3
2. pip3

## Setup

### Clone the project

```shell
git clone https://github.com/rahulkhatry4/Mapping-API.git
```

### Create a virtual environment with venv (install virtualenv, if its not installed) inside the project folder

```shell
cd Mapping-API
```
  
#### For Linux/Mac OSX

```shell
sudo apt-get install python3-venv
python3 -m venv venv
```
  
#### For Windows

```shell
pip install virtualenv
python -m venv venv
```

### Activate the virtual environment

#### For Linux/Mac OSX

```shell
source venv/bin/activate
```

#### For Windows

```shell
venv\Scripts\activate
```

#### Install the requirements

```shell
pip install -r requirements.txt
```

### Config your environment variables

Inside the `backend` folder create a file named as `.env` . Copy the contents of `.env_example` to `.env` and put your configuration there.

### Run the Migrations

```shell
python manage.py makemigrations
python manage.py migrate
```

### Run the development server

```
python manage.py runserver
```
