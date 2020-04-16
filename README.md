# weater-api

1. Create database  
    `createdb weather_api_db -O postgres`

2. Make first migration  
    `python manage.py migrate`

3. Populate a database  
    `python manage.py populate_users_group`  

4. Run django development server  
    `python manage.py runserver`