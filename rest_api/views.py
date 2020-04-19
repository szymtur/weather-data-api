import logging

from django.core.validators import ValidationError
from requests import HTTPError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_api import messages
from rest_api.permissions import OnlyAPIPermission, ApiKeyThrottle
from rest_api.serializers import WeatherSerializer
from rest_api.validators import lang_validator, units_validator, days_validator, ip_validator, coordinates_validator

from rest_api.helpers import (current_weather_data_helper, daily_weather_data_helper, reverse_geocode_data_helper,
                              forward_geocode_data_helper, api_exception_helper, lower_dict_keys_helper)

from rest_api.providers import (ip_info_handler, current_weather_provider, daily_weather_provider,
                                reverse_geocode_handler, forward_geocode_handler)


class CurrentWeatherView(APIView):
    permission_classes = [OnlyAPIPermission]
    throttle_classes = [ApiKeyThrottle]

    def get(self, request):
        try:
            request_GET = lower_dict_keys_helper(self.request.GET)

            city = request_GET.get('city')
            latitude = coordinates_validator(request_GET.get('lat'))
            longitude = coordinates_validator(request_GET.get('lon'))
            ip_address = ip_validator(request_GET.get('ip'))
            lang = lang_validator(request_GET.get('lang'))
            units = units_validator(request_GET.get('units'))

        except (ValidationError, Exception) as error:
            logging.error(error.message)
            return api_exception_helper(error.message, error.code)

        try:
            if city:
                geocode_data = forward_geocode_data_helper(forward_geocode_handler(city_name=city, lang=lang))
                wb_data = current_weather_provider(lat=geocode_data['lat'], lon=geocode_data['lon'],
                                                   units=units, lang=lang)

                weather_data, location_data = current_weather_data_helper(wb_data)
                location_data['address'] = geocode_data.get('address')

            elif latitude and longitude:
                wb_data = current_weather_provider(lat=latitude, lon=longitude, units=units, lang=lang)
                weather_data, location_data = current_weather_data_helper(wb_data)

                geocode_data = reverse_geocode_handler(lat=latitude, lon=longitude, lang=lang)
                location_data['address'] = reverse_geocode_data_helper(geocode_data)

            elif ip_address:
                ip_info = ip_info_handler(ip_address)
                wb_data = current_weather_provider(lat=ip_info.latitude, lon=ip_info.longitude, units=units, lang=lang)
                weather_data, location_data = current_weather_data_helper(wb_data)

                geocode_data = reverse_geocode_handler(lat=ip_info.latitude, lon=ip_info.longitude, lang=lang)
                location_data['address'] = reverse_geocode_data_helper(geocode_data)

            else:
                logging.error(messages.INVALID_PARAMETERS)
                return api_exception_helper(messages.INVALID_PARAMETERS, status.HTTP_400_BAD_REQUEST)

        except ValidationError as error:
            logging.error(error.message)
            return api_exception_helper(error.message, error.code)
        except (HTTPError, Exception) as error:
            logging.error(error)
            return api_exception_helper(messages.INTERNAL_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = WeatherSerializer(data={'location': location_data, 'weather': weather_data})

        if serializer.is_valid():
            return Response(serializer.data)

        logging.error(serializer.errors)
        return api_exception_helper(messages.INTERNAL_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR)


class DailyWeatherView(APIView):
    permission_classes = [OnlyAPIPermission]
    throttle_classes = [ApiKeyThrottle]

    def get(self, request):
        try:
            request_GET = lower_dict_keys_helper(self.request.GET)

            city = request_GET.get('city')
            latitude = coordinates_validator(request_GET.get('lat'))
            longitude = coordinates_validator(request_GET.get('lon'))
            ip_address = ip_validator(request_GET.get('ip'))
            days = days_validator(request_GET.get('days'))
            lang = lang_validator(request_GET.get('lang'))
            units = units_validator(request_GET.get('units'))

        except (ValidationError, Exception) as error:
            logging.error(error.message)
            return api_exception_helper(error.message, error.code)

        try:
            if city:
                geocode_data = forward_geocode_data_helper(forward_geocode_handler(city_name=city, lang=lang))
                wb_data = daily_weather_provider(lat=geocode_data['lat'], lon=geocode_data['lon'],
                                                 units=units, lang=lang, days=days)

                weather_data, location_data = daily_weather_data_helper(wb_data)
                location_data['address'] = geocode_data['address']

            elif latitude and longitude:
                wb_data = daily_weather_provider(lat=latitude, lon=longitude, units=units, lang=lang, days=days)
                weather_data, location_data = daily_weather_data_helper(wb_data)

                geocode_data = reverse_geocode_handler(lat=latitude, lon=longitude, lang=lang)
                location_data['address'] = reverse_geocode_data_helper(geocode_data)

            elif ip_address:
                ip_info = ip_info_handler(ip_address)
                wb_data = daily_weather_provider(lat=ip_info.latitude, lon=ip_info.longitude,
                                                 units=units, lang=lang, days=days)
                weather_data, location_data = daily_weather_data_helper(wb_data)

                geocode_data = reverse_geocode_handler(lat=ip_info.latitude, lon=ip_info.longitude, lang=lang)
                location_data['address'] = reverse_geocode_data_helper(geocode_data)

            else:
                logging.error(messages.INVALID_PARAMETERS)
                return api_exception_helper(messages.INVALID_PARAMETERS, status.HTTP_400_BAD_REQUEST)

        except ValidationError as error:
            logging.error(error.message)
            return api_exception_helper(error.message, error.code)
        except (HTTPError, Exception) as error:
            logging.error(error)
            return api_exception_helper(messages.INTERNAL_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = WeatherSerializer(data={'location': location_data, 'weather': weather_data})

        if serializer.is_valid():
            return Response(serializer.data)

        logging.error(serializer.errors)
        return api_exception_helper(messages.INTERNAL_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR)
