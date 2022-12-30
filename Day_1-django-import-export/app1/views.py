from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic import ListView, FormView

from .models import Student
from .forms import SelectFormatForm
from .admin import StudentResource


#Day 1
class StudentListView(ListView, FormView):
    """Getting objects list and exporting files to download."""
    model = Student
    template_name = 'app1/index.html'
    form_class = SelectFormatForm

    def post(self, request, **kwargs):
        """Accepting data from post request and creatingvrequired response to download files."""
        qs = self.get_queryset()
        dataset = StudentResource().export(qs)

        format = request.POST.get('format')

        match format:
            case 'csv' :
                ds = dataset.csv
            case 'xls' :
                ds = dataset.xls
            case 'json' :
                ds = dataset.json
        
        response =HttpResponse(ds, content_type = f"{format}")
        response['Content-Disposition'] = f"attachment; filename=students.{format}"
        return response
