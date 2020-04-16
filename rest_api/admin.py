from django import forms
from django.db import models
from django.contrib import admin

from weather_api import settings
from rest_api.helpers import api_key_generator
from rest_api.models import Configuration, ApiKeys


@admin.register(ApiKeys)
class ApiKeysAdmin(admin.ModelAdmin):
    list_display = ['api_key', 'key_name', 'day_limit', 'user']
    fields = ['api_key', 'key_name', 'day_limit', 'user']
    ordering = ['user']
    search_fields = ['api_key']

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'vTextField',
                                                            'style': 'background: #dddddd'})},
        models.TextField: {'widget': forms.TextInput(attrs={'class': 'vTextField'})},
    }

    def get_changeform_initial_data(self, request):
        return {'api_key': api_key_generator(),
                'key_name': settings.DEFAULT_API_KEY_NAME,
                'day_limit': settings.DEFAULT_API_KEY_LIMIT}


@admin.register(Configuration)
class ApiKeysAdmin(admin.ModelAdmin):
    list_display = ['code_name', 'api_key', 'description']
    fields = ['code_name', 'api_key', 'description']
    ordering = ['code_name']
    search_fields = ['code_name']
