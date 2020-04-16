from abc import abstractmethod
from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):

    location = serializers.JSONField()
    weather = serializers.JSONField()

    @abstractmethod
    def fake_abstract_method(self):
        """
        Fixes the warning: 'Class WeatherSerializer must implement all abstract methods'.
        """
        return
