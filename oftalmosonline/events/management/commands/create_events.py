from django.core.management.base import BaseCommand
from csv import DictReader
from oftalmosonline.events.models import Event
from oftalmosonline.users.models import User

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)
        parser.add_argument('author_email', type=str)

    def handle(self, *args, **options):
        file_name = options['file_name']
        author_email=options['author_email']
        user = User.objects.get(email=author_email)
        with open(file_name, 'r') as read_obj:
            csv_reader = DictReader(read_obj)
            for row in csv_reader:
                
                title = row['title']
                
                description=row['description']
                status=row['status']
                event_format=row['event_format']
                language=row['language']
                url=row['url']
                date_start=row['date_start']
                date_finish=row['date_finish']
                cme=row['cme']   
                
                Event.objects.create(
                    user = user,   
                    title = title,
                    description=description,
                    status=status,
                    event_format=event_format,
                    main_language=language,
                    event_url=url,
                    event_date_start=date_start,
                    event_date_finish=date_finish,
                    is_cme=cme)
        