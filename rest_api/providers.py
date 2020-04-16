import logging
from json import JSONDecodeError
from ipinfo import getHandler
from requests import get, HTTPError

from .models import Configuration


# ip geolocation - getting current position from ip address using https://ipinfo.io
def ip_info_handler(ip_address):
    try:
        api_key = Configuration.objects.get(code_name='ip_info_io').api_key
        return getHandler(api_key).getDetails(ip_address)
    except (HTTPError, Exception) as error:
        logging.error(error)
        raise HTTPError(error)


# reverse geocode - getting city name from latitude and longitude using http://openstreetmap.org
def reverse_geocode_handler(**kwargs):
    try:
        url = 'https://nominatim.openstreetmap.org/reverse'
        params = dict(format='json', **kwargs)
        return get(url, params=params).json()
    except (JSONDecodeError, Exception) as error:
        logging.error(error)
        raise HTTPError(error)


# forward geocode - getting latitude and longitude from city name using http://openstreetmap.org
def forward_geocode_handler(city_name):
    try:
        url = 'https://nominatim.openstreetmap.org'
        params = dict(format='json', limit=1, addressdetails=1, q=city_name)
        return get(url, params=params).json()
    except (JSONDecodeError, Exception) as error:
        logging.error(error)
        raise HTTPError(error)


# current weather - getting weather forecast from coordinates using https://weatherbit.io
def current_weather_provider(**kwargs):
    try:
        url = 'https://api.weatherbit.io/v2.0/current'
        params = dict(key=Configuration.objects.get(code_name='weather_bit').api_key, **kwargs)
        return get(url, params=params).json()
    except (HTTPError, Exception) as error:
        logging.error(error)
        raise HTTPError(error)


# next days weather - getting daily weather forecast from coordinates using https://weatherbit.io
def daily_weather_provider(**kwargs):
    try:
        url = 'https://api.weatherbit.io/v2.0/forecast/daily'
        params = dict(key=Configuration.objects.get(code_name='weather_bit').api_key, **kwargs)
        return get(url, params=params).json()
    except (HTTPError, Exception) as error:
        logging.error(error)
        raise HTTPError(error)
