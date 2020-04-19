from rest_framework import status
from rest_framework.exceptions import APIException

from rest_api import messages


class LimitExtendedError(APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = {'error': messages.API_KEY_LIMIT_EXCEED, 'code': status.HTTP_429_TOO_MANY_REQUESTS}
    default_code = 'too_many_requests'


class InvalidApiKeyError(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {'error': messages.API_KEY_NOT_VALID, 'code': status.HTTP_403_FORBIDDEN}
    default_code = 'forbidden'
