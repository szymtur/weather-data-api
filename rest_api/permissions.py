import logging

from datetime import date

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions, throttling

from rest_api import messages
from rest_api.models import ApiKeys, Throttling
from rest_api.errors import InvalidApiKeyError, LimitExtendedError


class OnlyAPIPermission(permissions.BasePermission):
    """
    Allows access only to users with valid api key.
    """
    def has_permission(self, request, view):
        if ApiKeys.objects.filter(api_key=request.GET.get('key')).exists():
            return True

        logging.error(messages.API_KEY_NOT_VALID)
        raise InvalidApiKeyError()


class ApiKeyThrottle(throttling.BaseThrottle):
    """
    Controls the rate of requests that clients can make to an API.
    """
    def allow_request(self, request, view):
        api_key = ApiKeys.objects.select_related('throttling').filter(api_key=request.GET.get('key')).first()

        try:
            api_key_throttling = api_key.throttling

        except ObjectDoesNotExist:
            api_key_throttling = Throttling(api_key=api_key)
            api_key_throttling.save()
            return True

        if api_key_throttling.date == date.today() and api_key_throttling.counter < api_key.day_limit:
            api_key_throttling.counter += 1
            api_key_throttling.save()
            return True

        if api_key_throttling.date < date.today():
            api_key_throttling.counter = 1
            api_key_throttling.save()
            return True

        logging.error(messages.API_KEY_LIMIT_EXCEED)
        raise LimitExtendedError()
