from django.db import models
from django.contrib.auth.models import User


class Configuration(models.Model):
    code_name = models.SlugField(max_length=64, blank=False, null=False)
    api_key = models.CharField(max_length=64, blank=False, null=False)
    description = models.CharField(max_length=128, blank=False, null=False)

    def __str__(self):
        return self.code_name


class ApiKeys(models.Model):
    api_key = models.CharField(max_length=64, unique=True, blank=False, null=False)
    day_limit = models.IntegerField(blank=False, null=False)
    key_name = models.TextField(max_length=64, blank=False, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.api_key

    class Meta:
        verbose_name_plural = 'Api Keys'


class Throttling(models.Model):
    api_key = models.OneToOneField(ApiKeys, on_delete=models.CASCADE, primary_key=True)
    date = models.DateField(auto_now=True)
    counter = models.IntegerField(default=1)
