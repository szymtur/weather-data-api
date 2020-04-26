import logging

from datetime import datetime
from pytz import timezone
from requests import HTTPError

from django.core.validators import ValidationError
from django.utils.crypto import get_random_string

from rest_framework import status
from rest_framework.response import Response

from rest_api import messages
from rest_api.models import ApiKeys


def reverse_geocode_data_helper(data):
    error = data.get('error')
    data = data.get('address')

    if error == messages.UNABLE_TO_GEOCODE:
        raise ValidationError(message=messages.INVALID_PARAMETERS, code=status.HTTP_400_BAD_REQUEST)

    if not data:
        logging.error(error.get('message'))
        raise HTTPError(error.get('message'))
    return data


def forward_geocode_data_helper(data):
    if isinstance(data, list) and not len(data):
        raise ValidationError(message=messages.NOT_FOUND, code=status.HTTP_404_NOT_FOUND)

    if not data:
        logging.error(messages.INVALID_PARAMETERS)
        raise HTTPError(messages.INVALID_PARAMETERS)

    try:
        return dict(address=data[0]['address'], lat=data[0]['lat'], lon=data[0]['lon'])
    except KeyError as error:
        logging.error(messages.KEY_ERROR + str(error))
        raise Exception(messages.KEY_ERROR + str(error))


def current_weather_data_helper(data):
    error = data.get('error')
    data = data.get('data')

    if not data:
        logging.error(error)
        raise HTTPError(error)

    weather_info = dict(temp=data[0]['temp'], realfeel_temp=data[0]['app_temp'],
                        pressure=data[0]['pres'], hmidity=data[0]['rh'],
                        wind=data[0]['wind_spd'], air_ql=data[0]['aqi'],
                        sunrise=data[0]['sunrise'], sunset=data[0]['sunset'], clouds=data[0]['clouds'],
                        last_ob_time=data[0]['last_ob_time'], uv_index=data[0]['uv'],
                        weather=data[0]['weather'])

    time = datetime.now(timezone(data[0]['timezone'])).strftime("%H:%M:%S")
    date = datetime.now(timezone(data[0]['timezone'])).strftime("%d-%m-%Y")

    location_info = dict(city_name=data[0]['city_name'], country_code=data[0]['country_code'],
                         timezone=data[0]['timezone'], time=time, date=date,
                         latitude=data[0]['lat'], longitude=data[0]['lon'])

    return weather_info, location_info


def daily_weather_data_helper(data):
    error = data.get('error')
    weather_data = data.get('data')

    if not weather_data:
        logging.error(error)
        raise HTTPError(error)

    weather_info = [dict(temp=el['temp'], max_temp=el['max_temp'], min_temp=el['min_temp'],
                         pressure=el['pres'], hmidity=el['rh'], wind=el['wind_spd'],
                         sunrise=el['sunrise_ts'], sunset=el['sunset_ts'],
                         uv_index=el['uv'], clouds=el['clouds'],
                         datetime=el['valid_date'], weather=el['weather']) for el in weather_data]

    time = datetime.now(timezone(data['timezone'])).strftime("%H:%M:%S")
    date = datetime.now(timezone(data['timezone'])).strftime("%d-%m-%Y")

    location_info = dict(city_name=data['city_name'], country_code=data['country_code'],
                         timezone=data['timezone'], time=time, date=date,
                         latitude=data['lat'], longitude=data['lon'])

    return weather_info, location_info


def api_key_generator():
    api_key = None

    is_not_uniq = True
    while is_not_uniq:
        api_key = get_random_string(length=32)
        is_not_uniq = ApiKeys.objects.filter(api_key=api_key).exists()
    return api_key


def api_exception_helper(message, status_code):
    return Response(data={'error': message, 'code': str(status_code)}, status=status_code)


def lower_dict_keys_helper(dictionary):
    return dict((key.lower(), val) for key, val in dictionary.items())
