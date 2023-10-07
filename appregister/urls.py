from django.urls import path
from .views import login1, registration

urlpatterns = [
    path('', login1, name="login"),
    path('registration/', registration, name="registration"),
]