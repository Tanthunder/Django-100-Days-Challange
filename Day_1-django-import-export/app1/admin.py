from django.contrib import admin

from import_export import resources
from  import_export.fields import Field

from .models import Student


#day1
class StudentResource(resources.ModelResource):
    """Resource class for import_export. Will be used  in views.py."""
    is_studying = Field()
    
    class Meta:
        model = Student
        fields = ('name','age','is_studying','created')
        export_order = ('name','age','is_studying','created')

    def dehydrate_is_studying(self,obj):
        """Similar to get_fieldname in drf"""
        if obj.is_studying:
            return 'yes'
        return 'no'

admin.site.register(Student)