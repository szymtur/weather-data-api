# Weather Data Api

The weather-data-api deliver accurate weather information for any location on Earth in lightweight JSON format.  
Weather-data-api provides current weather observations and daily weather forecasts for 12 days,  
for any point on the globe along with local timezone.


### Weather data can be fetched by:
  * city name, postal code, POI (point of interest) or address
  * geographical coordinates
  * ip address


### Service access:
  * [sign up](https://weather-forecast-data.herokuapp.com/account/signup/)  for an account
  * use the api key provided in account [dashboard](https://weather-forecast-data.herokuapp.com/account/dashboard/)


## Current Weather Data
This api returns current weather conditions for any location on Earth.  
Every api request will return the nearest, and most recent observation.


### Base url
> `https://weather-forecast-data.herokuapp.com/api/v1.0/current/`

### Request parameters

> #### required parameters:
> `key` - api key  
>
> #### optional parameters:
> `lang` - language  
> `units` - units  


### Search by city

> #### parameters:
> `city` - city name, postal code, point of interest or address. Can be not only in English.
>
> #### example requests:
> `https://weather-forecast-data.herokuapp.com/api/v1.0/current/?key=API_KEY&city=Tampa`
>
> `https://weather-forecast-data.herokuapp.com/api/v1.0/current/?key=API_KEY&city=30-549`
>
> `https://weather-forecast-data.herokuapp.com/api/v1.0/current/?key=API_KEY&city=sears-tower`


### Search by coordinates

> #### parameters:
> `lat, lon` - geographical coordinates of the location  
>
> #### example request:
> `https://weather-forecast-data.herokuapp.com/api/v1.0/current/?key=API_KEY&lat=50.25&lon=20.25`


### Search by ip address

> #### parameters:
> `ip` - ip address for geolocation  
>
> #### example request:
> `https://weather-forecast-data.herokuapp.com/api/v1.0/current/?key=API_KEY&ip=44.163.22.45`


### Example response

```
{
    "location": {
        "city_name": "Capellades",
        "country_code": "CR",
        "timezone": "America/Costa_Rica",
        "time": "11:42:38",
        "date": "18-04-2020",
        "latitude": 9.87,
        "longitude": -83.8,
        "address": {
            "city": "Santiago",
            "county": "Cantón Paraíso",
            "state": "Cartago Province",
            "postcode": "30202",
            "country": "Costa Rica",
            "country_code": "cr"
        }
    },
    "weather": {
        "temp": 24.4,
        "realfeel_temp": 24.6,
        "pressure": 888.3,
        "hmidity": 62,
        "wind": 5.81,
        "air_ql": 39,
        "sunrise": "11:23",
        "sunset": "23:47",
        "clouds": 1,
        "ob_time": "2020-04-18T17:13:00",
        "uv_index": 11.4034,
        "weather": {
            "icon": "c01d",
            "code": "800",
            "description": "Clear sky"
        }
    }
}
```


## 12 Days / Daily Forecast Data
This api returns a 12 days forecast in one day intervals for for any location on Earth.


### Base url
> `https://weather-forecast-data.herokuapp.com/api/v1.0/daily/`


### Request parameters

> #### required parameters:
> `key` - api key  
>
> #### optional parameters:
> `lang` - language  
> `units` - units  
> `days` - number of days returned [from 1 to 12] - DEFAULT 12 DAYS  


### Search by city

> #### parameters:
> `city` - city name, postal code, point of interest or address. Can be not only in English.
>
> #### example requests:
> `https://weather-forecast-data.herokuapp.com/api/v1.0/daily/?key=API_KEY&city=Sydney`
>
> `https://weather-forecast-data.herokuapp.com/api/v1.0/daily/?key=API_KEY&city=00-950`
>
> `https://weather-forecast-data.herokuapp.com/api/v1.0/daily/?key=API_KEY&city=sears-tower`


### Search by coordinates

> #### parameters:
> `lat, lon` - geographical coordinates of the location  
>
> #### example request:
> `https://weather-forecast-data.herokuapp.com/api/v1.0/daily/?key=API_KEY&lat=40.25&lon=10.25`


### Search by ip address

> #### parameters:
> `ip` - ip address for geolocation  
>
> #### example request:
> `https://weather-forecast-data.herokuapp.com/api/v1.0/daily/?key=API_KEY&ip=44.163.22.45`


### Example response

```
{
    "location": {
        "city_name": "Chicago",
        "country_code": "US",
        "timezone": "America/Chicago",
        "time": "15:24:53",
        "date": "18-04-2020",
        "latitude": 41.88,
        "longitude": -87.64,
        "address": {
            "address29": "Willis Tower",
            "house_number": "233",
            "road": "South Wacker Drive",
            "neighbourhood": "Printer's Row",
            "suburb": "Loop",
            "city": "Chicago",
            "county": "Cook County",
            "state": "Illinois",
            "postcode": "60606",
            "country": "United States of America",
            "country_code": "us"
        }
    },
    "weather": [{
        "temp": 8.8,
        "max_temp": 12.1,
        "min_temp": 1.9,
        "pressure": 989.962,
        "hmidity": 64,
        "wind": 7.16038,
        "sunrise": 1587207778,
        "sunset": 1587256640,
        "uv_index": 6.20868,
        "clouds": 0,
        "datetime": "2020-04-18",
        "weather": {
            "icon": "c01d",
            "code": 800,
            "description": "Clear Sky"
        }
    }, {
        "temp": 7.7,
        "max_temp": 13.9,
        "min_temp": 2.9,
        "pressure": 986.623,
        "hmidity": 83,
        "wind": 4.22351,
        "sunrise": 1587294084,
        "sunset": 1587343108,
        "uv_index": 6.92149,
        "clouds": 52,
        "datetime": "2020-04-19",
        "weather": {
            "icon": "c03d",
            "code": 803,
            "description": "Broken clouds"
        }
    }]
}
```


## Units format

> #### description:
> Metric, scientific and imperial units are available.
>
> #### parameters:
> `M` - Metric [Celsius, m/s, mm] - DEFAULT  
> `S` - Scientific [Kelvin, m/s, mm]  
> `I` - Imperial [Fahrenheit, mph, in]
>
> #### example request:
> `https://weather-forecast-data.herokuapp.com/api/v1.0/daily/?key=API_KEY&city=Tampa&units=S`


## Language

> #### description:
> Translation is applied for address and description fields.
>
> #### parameters:
> `en` - English - DEFAULT
> `ar` - Arabic
> `az` - Azerbaijani
> `be` - Belorussian
> `bg` - Bulgarian
> `bs` - Bosnian
> `ca` - Catalan
> `cz` - Czech
> `da` - Danish
> `de` - German
> `fi` - Finnish
> `fr` - French
> `el` - Greek
> `et` - Estonian
> `hr` - Croatian
> `hu` - Hungarian
> `id` - Indonesian
> `it` - Italian
> `is` - Icelandic
> `kw` - Cornish
> `lt` - Lithuanian
> `nb` - Norwegian
> `nl` - Dutch
> `pl` - Polish
> `pt` - Portuguese
> `ro` - Romanian
> `ru` - Russian
> `sk` - Slovak
> `sl` - Slovenian
> `sr` - Serbian
> `sv` - Swedish
> `tr` - Turkish
> `uk` - Ukrainian
> `zh` - Chinese (Simplified)
> `zh-tw` - Chinese (Traditional)
>
> #### example request:
> `https://weather-forecast-data.herokuapp.com/api/v1.0/daily/?key=API_KEY&city=Tampa&lang=pl`


## Api error codes

```json
{
    "error": "Invalid parameters.",
    "code": "400"
}
```

```json
{
    "error": "API key not valid.",
    "code": "403"
}
```

```json
{
    "error": "Not found.",
    "code": "404"
}
```

```json
{
    "error": "API key rate limit exceeded.",
    "code": "429"
}
```

```json
{
    "error": "Internal server error.",
    "code": "500"
}
```


## Services used:

### Ip geolocation

> [`https://ipinfo.io/`](https://ipinfo.io/)
>
> IP Geolocation is the identification of the geographic location
> of an Internet-connected device, by using an ip address.

### Forward geocoding

> [`https://nominatim.org`](https://nominatim.org)
>
> Forward geocoding is the process of converting a place name like city name, postal code, 
> point of interest or address into geographical coordinates - latitude and longitude values.


### Reverse geocoding

> [`https://nominatim.org`](https://nominatim.org)
>
> Reverse Geocoding is the process of converting a latitude and longitude point into a human readable address.


### Weather forecast

> [`https://www.weatherbit.io/`](https://www.weatherbit.io/)
>
> This weather api deliver accurate weather data and weather forecasts for any for any location on Earth.


## Running application locally

1. Create an account in weatherbit.io service and get the api key  

   [`https://www.weatherbit.io/account/create`](https://www.weatherbit.io/account/create)


2. Create an account in ipinfo.io service and get the api key  

   [`https://ipinfo.io/signup`](https://ipinfo.io/signup)


3. Create database specifying `postgress` user as owner of the new database  

   ```
   $ createdb weather_api_db -O postgres
   ```


4. Update database configuration in `settings.py`

   ```
   DATABASES = {
       'default': {
           'HOST': '127.0.0.1',
           'NAME': 'weather_api_db',
           'USER': 'postgres',
           'PASSWORD': 'PASSWORD',
           'ENGINE': 'django.db.backends.postgresql_psycopg2'
       }
   }
   ```


5. Make first migration

   ```
   $ python manage.py migrate
   ```


6. Populate users group

   ```
   $ python manage.py populate_users_group
   ```


7. Populate configuration

   ```
   $ python manage.py populate_configurations

   Enter the weather_bit api key: YOUR_WEATHER_BIT_API_KEY
   Enter the ip_info api key: YOUR_IP_INFO_API_KEY
   ```


8. Run django development server  

   ```
   $ python manage.py runserver
   ```
