from django.core.management.base import BaseCommand

from rest_api.models import Configuration


class Command(BaseCommand):
    help = 'Populates weather_bit and ip_info configuration'

    def handle(self, *args, **options):
        weather_bit_api_key = input('Enter the weather_bit api key: ')
        ip_info_api_key = input('Enter the ip_info api key: ')

        if len(weather_bit_api_key) > 64 or len(ip_info_api_key) > 64:
            return self.stderr.write("Input value too long")

        try:
            Configuration.objects.create(api_key=weather_bit_api_key,
                                         description='weather forecast api - weatherbit.io',
                                         code_name='weather_bit')

            self.stdout.write(self.style.SUCCESS("Successfully added weather_bit configuration"))


            Configuration.objects.create(api_key=ip_info_api_key,
                                         description='geolocation by ip address api - ipinfo.io',
                                         code_name='ip_info_io')

            self.stdout.write(self.style.SUCCESS("Successfully added ip_info configuration"))

        except Exception as error:
            return self.stderr.write(str(error))
