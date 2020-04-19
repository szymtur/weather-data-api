import logging

from django.core.validators import ValidationError
from ipaddress import ip_address
from rest_framework import status

from rest_api import messages
from weather_api import settings


def lang_validator(lang):
    if not lang or lang.lower() not in settings.ALLOWED_LANG:
        return settings.DEFAULT_LANG.lower()
    return lang


def units_validator(units):
    if not units or units.lower() not in settings.ALLOWED_UNITS:
        return settings.DEFAULT_UNITS.lower()
    return units


def days_validator(days):
    if days:
        try:
            days = int(days)
        except ValueError:
            logging.error(messages.INVALID_PARAMETERS)
            raise ValidationError(message=messages.INVALID_PARAMETERS, code=status.HTTP_400_BAD_REQUEST)

        if int(days) not in set(range(1, settings.DEFAULT_DAYS_LIMIT + 1)):
            return settings.DEFAULT_DAYS_LIMIT
        return days
    return settings.DEFAULT_DAYS_LIMIT


def ip_validator(_ip_address):
    if _ip_address:
        try:
            ip_address(_ip_address)
        except ValueError:
            logging.error(messages.INVALID_PARAMETERS)
            raise ValidationError(message=messages.INVALID_PARAMETERS, code=status.HTTP_400_BAD_REQUEST)
        return _ip_address
    return _ip_address


def coordinates_validator(lat_lon):
    if lat_lon:
        try:
            float(lat_lon)
        except (ValueError, TypeError):
            logging.error(messages.INVALID_PARAMETERS)
            raise ValidationError(message=messages.INVALID_PARAMETERS, code=status.HTTP_400_BAD_REQUEST)
        return lat_lon
    return lat_lon
