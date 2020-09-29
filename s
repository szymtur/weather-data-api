[1mdiff --git a/README.md b/README.md[m
[1mindex c62a2f4..7ae37f5 100644[m
[1m--- a/README.md[m
[1m+++ b/README.md[m
[36m@@ -371,36 +371,43 @@[m [mThis api returns a 12 days forecast in one day intervals for for any location on[m
    ```[m
 [m
 [m
[31m-4. Update database configuration in `settings.py`[m
[32m+[m[32m4. Update debug property in `settings.py`[m
[32m+[m
[32m+[m[32m   ```[m
[32m+[m[32m   DEBUG = True[m
[32m+[m[32m   ```[m
[32m+[m
[32m+[m
[32m+[m[32m5. Update database configuration in `settings.py`[m
 [m
    ```[m
    DATABASES = {[m
        'default': {[m
            'HOST': '127.0.0.1',[m
[32m+[m[32m           'ENGINE': 'django.db.backends.postgresql_psycopg2',[m
            'NAME': 'weather_api_db',[m
            'USER': 'postgres',[m
[31m-           'PASSWORD': 'PASSWORD',[m
[31m-           'ENGINE': 'django.db.backends.postgresql_psycopg2'[m
[32m+[m[32m           'PASSWORD': 'PASSWORD'[m
        }[m
    }[m
    ```[m
 [m
 [m
[31m-5. Make first migration[m
[32m+[m[32m6. Make first migration[m
 [m
    ```[m
    $ python manage.py migrate[m
    ```[m
 [m
 [m
[31m-6. Populate users group[m
[32m+[m[32m7. Populate users group[m
 [m
    ```[m
    $ python manage.py populate_users_group[m
    ```[m
 [m
 [m
[31m-7. Populate configuration[m
[32m+[m[32m8. Populate configuration[m
 [m
    ```[m
    $ python manage.py populate_configurations[m
[36m@@ -410,7 +417,7 @@[m [mThis api returns a 12 days forecast in one day intervals for for any location on[m
    ```[m
 [m
 [m
[31m-8. Run django development server  [m
[32m+[m[32m9. Run django development server[m[41m  [m
 [m
    ```[m
    $ python manage.py runserver[m
[1mdiff --git a/weather_api/settings.py b/weather_api/settings.py[m
[1mindex 91e1811..ebe2fad 100644[m
[1m--- a/weather_api/settings.py[m
[1m+++ b/weather_api/settings.py[m
[36m@@ -14,6 +14,8 @@[m [mimport os[m
 import django_heroku[m
 import dj_database_url[m
 [m
[32m+[m[32mfrom django.core.management.utils import get_random_secret_key[m
[32m+[m
 [m
 # Build paths inside the project like this: os.path.join(BASE_DIR, ...)[m
 BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))[m
[36m@@ -24,7 +26,7 @@[m [mBASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))[m
 [m
 [m
 # SECURITY WARNING: keep the secret key used in production secret![m
[31m-SECRET_KEY = os.environ.get('SECRET_KEY')[m
[32m+[m[32mSECRET_KEY = os.environ.get('SECRET_KEY') or get_random_secret_key()[m
 [m
 [m
 # SECURITY WARNING: don't run with debug turned on in production![m
[36m@@ -89,6 +91,16 @@[m [mDATABASES = {[m
     'default': dj_database_url.config(conn_max_age=600, ssl_require=True)[m
 }[m
 [m
[32m+[m[32mDATABASES = {[m
[32m+[m[32m    'default': {[m
[32m+[m[32m        'HOST': '127.0.0.1',[m
[32m+[m[32m        'ENGINE': 'django.db.backends.postgresql_psycopg2',[m
[32m+[m[32m        'NAME': 'weather_api_db',[m
[32m+[m[32m        'USER': 'postgres',[m
[32m+[m[32m        'PASSWORD': 'coderslab'[m
[32m+[m[32m    }[m
[32m+[m[32m}[m
[32m+[m
 [m
 # Password validation[m
 # https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators[m
