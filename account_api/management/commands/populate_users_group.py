from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Populates rest_api_users group and adds permissions'

    def handle(self, *args, **options):
        permissions = ['view_user', 'change_user', 'delete_user', 'view_apikeys', 'change_apikeys', 'delete_apikeys']
        group_name = 'rest_api_users'

        role, created = Group.objects.get_or_create(name=group_name)
        self.stdout.write(self.style.SUCCESS("Successfully created rest_api_users group"))

        for permission in permissions:
            role.permissions.add(Permission.objects.get(codename=permission))
            self.stdout.write(self.style.SUCCESS(f'Successfully added {permission} permission to rest_api_users group'))
