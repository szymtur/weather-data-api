from rest_framework import status
from rest_framework.exceptions import APIException


class LimitExtendedError(APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = {'error': 'API key rate limit exceeded.', 'code': status.HTTP_429_TOO_MANY_REQUESTS}
    default_code = 'too_many_requests'


class InvalidApiKeyError(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {'error': 'API key not valid.', 'code': status.HTTP_403_FORBIDDEN}
    default_code = 'forbidden'
