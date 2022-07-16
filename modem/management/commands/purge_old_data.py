from django.core.management.base import BaseCommand, CommandError
from modem.models import AmtcModel 
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Delete objects older than 10 days'

    def handle(self, *args, **options):
        AmtcModel.objects.filter(vaqt__lte=datetime.now()-timedelta(hour=10)).delete()
        self.stdout.write('Deleted objects older than 10 days')