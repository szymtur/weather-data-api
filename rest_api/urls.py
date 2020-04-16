from django.urls import path

from rest_api.views import CurrentWeatherView, DailyWeatherView


urlpatterns = [
    path('api/v1.0/current/', CurrentWeatherView.as_view(), name='current_weather'),
    path('api/v1.0/daily/', DailyWeatherView.as_view(), name='daily_weather'),
]
