from django.utils.crypto import get_random_string

from rest_api.models import ApiKeys


def api_key_generator():
    api_key = None
    is_not_uniq = True
    while is_not_uniq:
        api_key = get_random_string(length=32)
        is_not_uniq = ApiKeys.objects.filter(api_key=api_key).exists()
    return api_key
