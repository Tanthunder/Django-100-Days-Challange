from django.core.management.base import BaseCommand
from app1.models import Student

class Command(BaseCommand):

    """Command class to get student with age and startwith filter."""
    help = 'j'

    def add_arguments(self, parser):
        """Adding arguments."""
        parser.add_argument('age', type=int, help='provide age')
        parser.add_argument('--startwith', type=str, help='provide starting character')

    def handle(self, *args, **options):
        """Entrypoint. Handles logic which needs to be executed when command executes."""
        age=options['age']
        starting = options['startwith']
        if starting:
            student_count = Student.objects.filter(age__gt = age, name__startswith = starting)
        else:
            student_count = Student.objects.filter(age__gt = age)
    
        print(student_count)
        

        
