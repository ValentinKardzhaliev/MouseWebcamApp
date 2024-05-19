# Mouse and Webcam App with Django

This application captures mouse movements and webcam images, saving data to an SQLite database.

## Setup

1. Clone the repository.
2. Move into the project directory
```bash 
cd MouseWebcamApp
```
4. Create a virtual environment:
```bash
python -m venv venv
```
3. Activate the virtual environment:
   
  Windows:
  ```bash
  venv\Scripts\activate
  ```
  Linux:
  ```bash
  source venv/bin/activate
  ```
4. Install the dependencies:
  ```bash
  pip install -r requirements.txt
  ```
5. Migrate the models to the database:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
6. Run the Django server:
  ```bash
  python manage.py runserver
  ```

Required packages:
```bash
  asgiref==3.8.1
  attrs==23.2.0
  autobahn==23.6.2
  Automat==22.10.0
  cffi==1.16.0
  channels==4.1.0
  constantly==23.10.4
  cryptography==42.0.7
  daphne==4.1.2
  Django==5.0.6
  hyperlink==21.0.0
  idna==3.7
  incremental==22.10.0
  msgpack==1.0.8
  numpy==1.26.4
  opencv-python-headless==4.9.0.80
  pillow==10.3.0
  pyasn1==0.6.0
  pyasn1_modules==0.4.0
  pycparser==2.22
  pyOpenSSL==24.1.0
  pyserial==3.5
  service-identity==24.1.0
  six==1.16.0
  sqlparse==0.5.0
  Twisted==24.3.0
  twisted-iocpsupport==1.0.4
  txaio==23.1.1
  typing_extensions==4.11.0
  tzdata==2024.1
  zope.interface==6.4
```
