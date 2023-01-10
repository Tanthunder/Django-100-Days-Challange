from django.core.management.base import BaseCommand
from app1.models import Student

class Command(BaseCommand):

    """Command class to create custom command."""
    help = 'Displays total number of students in Student model/table.'

    def handle(self, *args, **kwargs):
        """Entrypoint. Handles logic which needs to be executed when command executes."""
        student_count = Student.objects.all().count()
        print(student_count)