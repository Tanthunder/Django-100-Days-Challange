from django.urls import path
from  .views import StudentListView

app_name = "day_1_to_10"

urlpatterns = [
    path("",StudentListView.as_view(),name = 'index'),
]