from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from decouple import config

class Command(BaseCommand):
    help = 'Create superuser from environment variables'

    def handle(self, *args, **options):
        User = get_user_model()
        username = config('DJANGO_SUPERUSER_USERNAME', default='admin')
        email = config('DJANGO_SUPERUSER_EMAIL', default='musasachristopher2@gmail.com')
        password = config('DJANGO_SUPERUSER_PASSWORD', default=None)

        if not password:
            self.stdout.write('DJANGO_SUPERUSER_PASSWORD not set — skipping.')
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(f'Superuser "{username}" already exists — skipping.')
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(f'Superuser "{username}" created successfully.')