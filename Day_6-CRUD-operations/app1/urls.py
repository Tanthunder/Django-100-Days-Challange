
from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_all_data, name = 'all-data'),
    path('<int:pk>', views.read_specific_data, name = 'specific-data'),
    path('create_student', views.create_student, name = 'create_student'),
    path('update_student/<int:pk>', views.update_student, name = 'update_student'),
    path('delete_student/<int:pk>', views.delete_student, name = 'delete_student'),
]
