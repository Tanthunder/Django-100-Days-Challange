
from django.urls import path
from .views import verify, auth_view ,home

urlpatterns = [
    path('', home, name = 'home'),
    path('login/', auth_view, name = 'login'),
    path('verify/', verify, name = 'verify'),
]
